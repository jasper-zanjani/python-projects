import tkinter as tk
from tkinter import ttk

def main():
  win = tk.Tk()
  win.title("Great success")

  # Combining these lines produces an error
  # a_label = ttk.Label(win, text="A label").grid(column = 0, row = 0)
  a_label = ttk.Label(win, text="A label")
  a_label.grid(column = 0, row = 0)

  name = tk.StringVar()
  name_entered = ttk.Entry(win, width=12, textvariable=name)
  name_entered.grid(column=2, row=0)

  def click_me():
    action.configure(text=f"Hello {name.get()}")
    
    # Combining these lines also throws an `AtributeError`
    # a_label.configure(foreground='red').configure(text='A Red Label')
    a_label.configure(foreground='red')
    a_label.configure(text='A Red Label')

  action = ttk.Button(win, text='Click me!', command=click_me)
  action.grid(column=1, row=0)

  # Bring focus to textbox as soon as program runs (p. 22)
  name_entered.focus()

  win.mainloop()

if __name__ == '__main__':
  main()