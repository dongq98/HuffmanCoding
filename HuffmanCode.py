from collections import defaultdict
from Heap import *

# Node of Huffman tree.
class HuffmanNode:
  def __init__(self, left = None, right = None):
    self.left = left
    self.right = right

# Returns the frequencies of each characters in the text.
def getFrequencies(text):
  frequencies = defaultdict(int)
  for ch in text:
    frequencies[ch] += 1
  return frequencies

# Returns Huffman tree constructed from the frequency dictionary.
def encode(frequencies):
  p = Heap()
  # Construct priority queue with high priorities for low frequencies.
  for char, freq in frequencies.iteritems():
    p.insert((freq, char))
  # Construct Huffman tree.
  while len(p) > 1:
    left = p.pop()
    right = p.pop()
    node = HuffmanNode(left[1], right[1])
    p.insert((left[0] + right[0], node))
  return p.pop()[1]

# Returns Huffman encoded codebook from the Huffman Tree.
# Recursively calculates the correspoding codewords to each characters.
def getHuffmanCode(root):
  def traverseHuffmanTree(node, codebook, path):
    if node.left:
      path.append('0')
      if isinstance(node.left, HuffmanNode):
        traverseHuffmanTree(node.left, codebook, path)
      else:
        codebook[node.left] = ''.join(path)
      path.pop()
    if node.right:
      path.append('1')
      if isinstance(node.right, HuffmanNode):
        traverseHuffmanTree(node.right, codebook, path)
      else:
        codebook[node.right] = ''.join(path)
      path.pop()
    return codebook
  return traverseHuffmanTree(root, {}, [])

# Reconstructs Huffman tree from the codebook.
# Just follows the bits of each codewords to construct the tree.
def reconstructHuffmanTree(codebook):
  root = HuffmanNode()
  for char, code in codebook.iteritems():
    node = root
    for bit in code[:-1]:
      if bit == '0':
        if not node.left:
          node.left = HuffmanNode()
        node = node.left
      elif bit == '1':
        if not node.right:
          node.right = HuffmanNode()
        node = node.right
    if code[-1] == '0':
      node.left = char
    elif code[-1] == '1':
      node.right = char
  return root

# Returns Huffman code and compressed text.
def compress(text):
  codebook = getHuffmanCode(encode(getFrequencies(text)))
  return codebook, ''.join([codebook[char] for char in text])

# Returns decompressed text from the prefix code and the compressed text.
def decompress(codebook, data):
  root = reconstructHuffmanTree(codebook)
  node = root
  output = []
  for bit in data:
    if bit == '0':
      if isinstance(node.left, HuffmanNode):
        node = node.left
      else:
        output.append(node.left)
        node = root
    elif bit == '1':
      if isinstance(node.right, HuffmanNode):
        node = node.right
      else:
        output.append(node.right)
        node = root
  return ''.join(output)