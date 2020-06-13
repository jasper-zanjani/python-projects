import tkinter as tk
from tkinter import ttk, scrolledtext


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

    # Disable button after it is pressed, p. 23
    action.configure(state='disabled')

  action = ttk.Button(win, text='Click me!', command=click_me)
  action.grid(column=1, row=0)

  # Dropdown menu (p. 24)
  ttk.Label(win, text="Choose a number:").grid(column=3,row=0)
  number = tk.StringVar()
  number_chosen = ttk.Combobox(win, width=12,textvariable=number)
  number_chosen['values'] = (1, 2, 4, 42, 100)
  number_chosen.grid(column=3, row=1)
  number_chosen.current(0)

  # Checkboxes p. 27
  chVarDis = tk.IntVar()
  check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled')
  check1.select()
  check1.grid(column=0, row=4, sticky=tk.W)

  chVarUn = tk.IntVar()
  check2 = tk.Checkbutton(win, text="Unchecked", variable=chVarUn)
  check2.deselect()
  check2.grid(column=1, row=4, sticky=tk.W)

  chVarEn = tk.IntVar()
  check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
  check3.select()
  check3.grid(column=2, row=4, sticky=tk.W)

  # Radio buttons
  Blue = "Blue"
  Red = "Red"
  Gold = "Gold"

  def colorize(arg, color):
    arg.configure(background=color)
  
  def radCall():
    radSel = radVar.get()
    if radSel == 1: 
      for item in [win, rad1, rad2, rad3, check1, check2, check3, action, a_label]:
        colorize(item, Red)
    elif radSel == 2: 
      for item in [win, rad1, rad2, rad3, check1, check2, check3, action, a_label]:
        colorize(item, Blue)
    else: 
      for item in [win, rad1, rad2, rad3, check1, check2, check3, action, a_label]:
        colorize(item, Gold)

  radVar = tk.IntVar()
  rad1 = tk.Radiobutton(win, text=Red, variable=radVar, value=1, command=radCall)
  rad2 = tk.Radiobutton(win, text=Blue, variable=radVar, value=2, command=radCall)
  rad3 = tk.Radiobutton(win, text=Gold, variable=radVar, value=3, command=radCall)
  
  rad1.grid(column=0, row=5, sticky=tk.W, columnspan=3)
  rad2.grid(column=1, row=5, sticky=tk.W, columnspan=3)
  rad3.grid(column=2, row=5, sticky=tk.W, columnspan=3)

  # Textbox with scrollbar, p. 32
  textbox = scrolledtext.ScrolledText(win, width=30, height=5, wrap = tk.WORD)
  textbox.grid(column=0, columnspan=3)

  # Bring focus to textbox as soon as program runs (p. 22)
  name_entered.focus()
  win.resizable(False, False)
  win.mainloop()

if __name__ == '__main__':
  main()