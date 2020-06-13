import tkinter as tk
from tkinter import ttk, scrolledtext


def main():
  win = tk.Tk()
  win.title("Great success")

  # Method chaining produces an error
  # a_label = ttk.Label(win, text="A label").grid(column = 0, row = 0)
  a_label = ttk.Label(win, text="Enter a name:")
  a_label.grid(column = 0, row = 0)

  name = tk.StringVar()
  textbox = ttk.Entry(win, width=12, textvariable=name)
  textbox.grid(column=0, row=1)

  def click_me():
    button.configure(text=f"Hello {name.get()}")
    # Disable button after it is pressed, p. 23
    button.configure(state='disabled')

    # Method chaining throws an `AtributeError`
    # a_label.configure(foreground='red').configure(text='A Red Label')
    a_label.configure(foreground='red',text='Button is clicked!')

  button = ttk.Button(win, text='Click me!', command=click_me)
  button.grid(column=2, row=1)

  # Dropdown menu (p. 24)
  ttk.Label(win, text="Choose a number:").grid(column=1,row=0)
  number = tk.StringVar()
  dropdown = ttk.Combobox(win, width=12,textvariable=number)
  dropdown['values'] = (1, 2, 4, 42, 100)
  dropdown.grid(column=1, row=1)
  dropdown.current(0)

  # Checkboxes p. 27
  chVarDis = tk.IntVar()
  check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled')
  check1.select()
  check1.grid(column=0, row=4,)
  # The `sticky=tk.W` appears to change the margin between the element and the window border
  # check1.grid(column=0, row=4, sticky=tk.W)

  chVarUn = tk.IntVar()
  check2 = tk.Checkbutton(win, text="Unchecked", variable=chVarUn)
  check2.deselect()
  check2.grid(column=1, row=4, sticky=tk.W)

  chVarEn = tk.IntVar()
  check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
  check3.select()
  check3.grid(column=2, row=4, sticky=tk.W)

  # Radio buttons
  Blue, Red, Gold = "Blue", "Red", "Gold"

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
  
  rad1.grid(column=0, row=5)
  rad2.grid(column=1, row=5)
  rad3.grid(column=2, row=5)

  # rad1.grid(column=0, row=5, sticky=tk.W, columnspan=3)
  # rad2.grid(column=1, row=5, sticky=tk.W, columnspan=3)
  # rad3.grid(column=2, row=5, sticky=tk.W, columnspan=3)

  # Textbox with scrollbar, p. 32
  textbox = scrolledtext.ScrolledText(win, width=30, height=5, wrap = tk.WORD)
  textbox.grid(column=0, columnspan=3)

  # Labels, p. 38
  buttons_frame = ttk.LabelFrame(win, text='')
  buttons_frame.grid(column=0, row=7, padx=20, pady=40)
  ttk.Label(buttons_frame, text='Label1 - Once upon a midnight dreary, while I pondered weak and weary').grid(column=0, row=0, sticky=tk.W)
  ttk.Label(buttons_frame, text='Label2').grid(column=0, row=1, sticky=tk.W)
  ttk.Label(buttons_frame, text='Label3').grid(column=0, row=2, sticky=tk.W)

  # - `winfo_children()` method returns a list of all children, (p. 43)
  # - `grid_configure()` method allows modification of UI elements before 
  #    the main loop displays them
  for i in buttons_frame.winfo_children():
    i.grid_configure(padx=8, pady=4)

  # Bring focus to textbox as soon as program runs (p. 22)
  button.focus()
  win.resizable(False, False)
  win.mainloop()

if __name__ == '__main__':
  main()