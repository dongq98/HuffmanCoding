from Tkinter import *
from ttk import *
import tkFileDialog
import json

import HuffmanCode

class Application(Frame):

  # GUI settings
  def __init__(self):
    Frame.__init__(self)

    # App variables
    self.paths = {}
    self.files = {}
    self.paths['comp'] = StringVar()
    self.paths['dcmp'] = StringVar()
    self.paths['huff'] = StringVar()

    # Basic GUI settings
    self.master.title("Huffman Coding")
    self.master.resizable(width = FALSE, height = FALSE)
    self.grid()
    self.canvas = Canvas(self, width = 600, height = 600)
    self.canvas.grid(row = 0, column = 0)

    # Menus
    self.tabs = Notebook(self, width = 300, height = 600)
    self.comp = Frame(self.tabs)
    self.decomp = Frame(self.tabs)
    self.tabs.add(self.comp, text = 'Compress', sticky = W+E+N+S)
    self.tabs.add(self.decomp, text = 'Decompress')
    self.tabs.grid(row = 0, column = 1, pady = 5)

    # =========================
    #  Menu / Compression
    # =========================

    self.comp.grid_columnconfigure(0, weight = 1)

    # File input UI label frame
    self.comp.files = LabelFrame(self.comp, text = 'File input')
    self.comp.files.grid(row = 0, column = 0, padx = 7, pady = 5, ipady = 2, sticky = W+E)

    Label(self.comp.files, text = 'Input').grid(row = 0, column = 0)

    ## Open button
    self.comp.files.openButton = Button(self.comp.files, text = 'open', width = 0,
        command = lambda: self.openFile('comp'))
    self.comp.files.openButton.grid(row = 0, column = 1)

    ## Entry for displaying file path
    self.comp.files.inputPathEntry = Entry(self.comp.files, state = 'readonly',
        textvariable = self.paths['comp'])
    self.comp.files.inputPathEntry.grid(row = 0, column = 2, padx = 5, sticky = W+E)
    self.comp.files.grid_columnconfigure(2, weight = 1)

    # Compress button
    self.comp.execute = Button(self.comp, text = 'Compress!', command = self.compress)
    self.comp.execute.grid(row = 1, column = 0, padx = 5, pady = 2, sticky = W+E)

    # Text widgets
    ## Original text (before compressed)
    self.comp.original = Frame(self.comp)
    self.comp.original.grid(row = 2, column = 0, pady = 2, stick = W+E+N+S)
    self.comp.original.grid_rowconfigure(0, weight = 1)
    self.comp.original.grid_columnconfigure(0, weight = 1)
    self.comp.original.scroll = Scrollbar(self.comp.original)
    self.comp.original.scroll.grid(row = 0, column = 1, stick = N+S)
    self.comp.original.box = Text(self.comp.original,
        yscrollcommand = self.comp.original.scroll.set)
    self.comp.original.box.grid(row = 0, column = 0, stick = W+E+N+S)
    self.comp.original.scroll.config(command = self.comp.original.box.yview)
    self.comp.grid_rowconfigure(2, weight = 1)

    ## Compressed text
    self.comp.compressed = Frame(self.comp)
    self.comp.compressed.grid(row = 3, column = 0, pady = 2, stick = W+E+N+S)
    self.comp.compressed.grid_rowconfigure(0, weight = 1)
    self.comp.compressed.grid_columnconfigure(0, weight = 1)
    self.comp.compressed.scroll = Scrollbar(self.comp.compressed)
    self.comp.compressed.scroll.grid(row = 0, column = 1, stick = N+S)
    self.comp.compressed.box = Text(self.comp.compressed,
        yscrollcommand = self.comp.compressed.scroll.set)
    self.comp.compressed.box.grid(row = 0, column = 0, stick = W+E+N+S)
    self.comp.compressed.scroll.config(command = self.comp.compressed.box.yview)
    self.comp.grid_rowconfigure(3, weight = 1)

    # =========================
    #  Menu / Decompression
    # =========================

    self.decomp.grid_columnconfigure(0, weight = 1)

    # File input UI label frame
    self.decomp.files = LabelFrame(self.decomp, text = 'File input')
    self.decomp.files.grid(row = 0, column = 0, padx = 7, pady = 5, ipady = 2, sticky = W+E)

    ## Compressed file
    Label(self.decomp.files, text = 'Compressed').grid(row = 0, column = 0)

    self.decomp.files.openButton = Button(self.decomp.files, text = 'open', width = 0,
        command = lambda: self.openFile('dcmp'))
    self.decomp.files.openButton.grid(row = 0, column = 1)

    self.decomp.files.inputPathEntry = Entry(self.decomp.files, state = 'readonly',
        textvariable = self.paths['dcmp'])
    self.decomp.files.inputPathEntry.grid(row = 0, column = 2, padx = 5, sticky = W+E)
    self.decomp.files.grid_columnconfigure(2, weight = 1)

    ## Huffman code file
    Label(self.decomp.files, text = 'Huffman code').grid(row = 1, column = 0)

    self.decomp.files.openButton = Button(self.decomp.files, text = 'open', width = 0,
        command = lambda: self.openFile('huff'))
    self.decomp.files.openButton.grid(row = 1, column = 1)

    self.decomp.files.inputPathEntry = Entry(self.decomp.files, state = 'readonly',
        textvariable = self.paths['huff'])
    self.decomp.files.inputPathEntry.grid(row = 1, column = 2, padx = 5, sticky = W+E)
    self.decomp.files.grid_columnconfigure(2, weight = 1)

    # Compress button
    self.decomp.execute = Button(self.decomp, text = 'Decompress!', command = self.decompress)
    self.decomp.execute.grid(row = 1, column = 0, padx = 5, pady = 2, sticky = W+E)

    # Text widgets
    ## Decompressed text
    self.decomp.decompressed = Frame(self.decomp)
    self.decomp.decompressed.grid(row = 2, column = 0, pady = 2, stick = W+E+N+S)
    self.decomp.decompressed.grid_rowconfigure(0, weight = 1)
    self.decomp.decompressed.grid_columnconfigure(0, weight = 1)
    self.decomp.decompressed.scroll = Scrollbar(self.decomp.decompressed)
    self.decomp.decompressed.scroll.grid(row = 0, column = 1, stick = N+S)
    self.decomp.decompressed.box = Text(self.decomp.decompressed,
        yscrollcommand = self.decomp.decompressed.scroll.set)
    self.decomp.decompressed.box.grid(row = 0, column = 0, stick = W+E+N+S)
    self.decomp.decompressed.scroll.config(command = self.decomp.decompressed.box.yview)
    self.decomp.grid_rowconfigure(2, weight = 1)

    ## Compressed text
    self.decomp.compressed = Frame(self.decomp)
    self.decomp.compressed.grid(row = 3, column = 0, pady = 2, stick = W+E+N+S)
    self.decomp.compressed.grid_rowconfigure(0, weight = 1)
    self.decomp.compressed.grid_columnconfigure(0, weight = 1)
    self.decomp.compressed.scroll = Scrollbar(self.decomp.compressed)
    self.decomp.compressed.scroll.grid(row = 0, column = 1, stick = N+S)
    self.decomp.compressed.box = Text(self.decomp.compressed,
        yscrollcommand = self.decomp.compressed.scroll.set)
    self.decomp.compressed.box.grid(row = 0, column = 0, stick = W+E+N+S)
    self.decomp.compressed.scroll.config(command = self.decomp.compressed.box.yview)
    self.decomp.grid_rowconfigure(3, weight = 1)


  def display(self, textBox, text):
    textBox.delete("1.0", END)
    textBox.insert("1.0", text)

  def openFile(self, fileType):
    try:
      self.paths[fileType].set(tkFileDialog.askopenfilename())
    except IOError:
      return
    self.files[fileType] = open(self.paths[fileType].get(), 'r').read()
    if fileType == 'comp':
      self.display(self.comp.original.box, self.files[fileType])
    elif fileType == 'dcmp':
      self.display(self.decomp.compressed.box, self.files[fileType])
    else:  # fileType == 'huff'
      # self.drawHuffmanTree(root)

  def drawHuffmanTree(self, root):
    pass

  def compress(self):
    if 'comp' in self.files:  # If a file to be compressed is open
      self.codebook, self.compressed = HuffmanCode.compress(self.files['comp'])
      try:
        map(unicode, self.codebook)
      except UnicodeDecodeError:
        print 'Unicode decode error'
        return  # TODO: Show error message

      open(self.paths['comp'].get()+'.comp', 'w').write(self.compressed)
      open(self.paths['comp'].get()+'.huff', 'w').write(json.dumps(self.codebook))
      self.display(self.comp.compressed.box, self.compressed)
      self.drawHuffmanTree(HuffmanCode.reconstructHuffmanTree(self.codebook))

  def decompress(self):
    pass


def main():
  Application().mainloop()

if __name__ == '__main__':
  main()