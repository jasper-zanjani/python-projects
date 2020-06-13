import tkinter as tk
from tkinter import ttk

def main():
  window = tk.Tk()
  window.title("Python GUI")

  # Tab controls, p. 63
  tabControl = ttk.Notebook(window)
  tab1 = ttk.Frame(tabControl)
  tabControl.add(tab1, text='Tab 1')
  tabControl.pack(expand=1, fill='both')

  window.mainloop()

if __name__ == '__main__':
  main()