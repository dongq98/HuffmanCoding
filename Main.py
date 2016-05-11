from Tkinter import *
from ttk import *
import tkFileDialog
import json

import HuffmanCode

class Application(Frame):
  # GUI settings
  def __init__(self):
    Frame.__init__(self)

    self.paths = {}
    self.files = {}
    self.paths['comp'] = StringVar()
    self.paths['dcmp'] = StringVar()
    self.paths['huff'] = StringVar()

    # Basic settings
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

    # Menu / Compression
    self.comp.grid_columnconfigure(0, weight = 1)
    self.comp.grid_rowconfigure(2, weight = 1)
    self.comp.grid_rowconfigure(3, weight = 1)
    self.comp.files = LabelFrame(self.comp, text = 'File input')
    self.comp.files.grid(row = 0, column = 0, padx = 7, pady = 5, ipady = 2, sticky = W+E)

    self.comp.files.grid_columnconfigure(2, weight = 1)
    Label(self.comp.files, text = 'Input').grid(row = 0, column = 0)
    self.comp.files.openInput = Button(self.comp.files, text = 'open', width = 0,
        command = lambda: self.openFile('comp'))
    self.comp.files.inputPathEntry = Entry(self.comp.files, state = 'readonly',
        textvariable = self.paths['comp'])
    self.comp.files.openInput.grid(row = 0, column = 1)
    self.comp.files.inputPathEntry.grid(row = 0, column = 2, padx = 5, sticky = W+E)

    self.comp.execute = Button(self.comp, text = 'Compress!', command = self.compress)
    self.comp.execute.grid(row = 1, column = 0, padx = 5, pady = 2, sticky = W+E)

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

  def display(self, textBox, text):
    textBox.delete("1.0", END)
    textBox.insert("1.0", text)

  def openFile(self, fileType):
    try:
      self.paths[fileType].set(tkFileDialog.askopenfilename())
      self.files[fileType] = open(self.paths[fileType].get(), 'r').read()
      self.display(self.comp.original.box, self.files[fileType])
      return True
    except:
      return False

  def displayHuffmanTree(self, root):
    pass

  def compress(self):
    if 'comp' in self.files:
      self.codebook, self.compressed = HuffmanCode.compress(self.files['comp'])
      open(self.paths['comp'].get()+'.comp', 'w').write(self.compressed)
      open(self.paths['comp'].get()+'.huff', 'w').write(json.dumps(self.codebook))
      self.display(self.comp.compressed.box, self.compressed)
      self.displayHuffmanTree(HuffmanCode.reconstrucHuffmanTree(self.codebook))


def main():
  Application().mainloop()

if __name__ == '__main__':
  main()