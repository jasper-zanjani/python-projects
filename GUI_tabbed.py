import tkinter as tk
from tkinter import ttk

def main():
  window = tk.Tk()
  window.title("Python GUI")


  # Tab controls, p. 63
  tabControl = ttk.Notebook(window)
  
  tab1 = ttk.Frame(tabControl)
  tabControl.add(tab1, text='Tab 1')

  mighty = ttk.LabelFrame(tab1, text=" Mighty Python") # p. 64
  mighty.grid(column = 0, row = 0, padx=8, pady=4)

  a_label = ttk.Label(mighty, text="Enter a name:")
  a_label.grid(column = 0, row = 0, sticky = 'W')
  
  tab2 = ttk.Frame(tabControl)
  tabControl.add(tab2, text='Tab 2')
  
  tabControl.pack(expand=1, fill='both')

  window.mainloop()

if __name__ == '__main__':
  main()