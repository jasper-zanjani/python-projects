import tkinter as tk
from tkinter import ttk, scrolledtext


def main():
  win = tk.Tk()
  win.title("Great success")

  mighty = ttk.LabelFrame(win, text=' Mighty Python ')
  mighty.grid(column=0, row=0, padx=8, pady=4)

  # Method chaining produces an error
  # a_label = ttk.Label(win, text="A label").grid(column = 0, row = 0)
  a_label = ttk.Label(mighty, text="Enter a name:")
  a_label.grid(column = 0, row = 0, sticky=(tk.W, tk.E))

  name = tk.StringVar()
  textbox = ttk.Entry(mighty, width=12, textvariable=name)
  textbox.grid(column=0, row=1, sticky=(tk.W,tk.E))

  def click_me():
    button.configure(text=f"Hello {name.get()}")
    button.configure(state='disabled') # Disable button after it is pressed, p. 23

    # Method chaining throws an `AtributeError`
    # a_label.configure(foreground='red').configure(text='A Red Label')
    a_label.configure(foreground='red',text='Button is clicked!')

  button = ttk.Button(mighty, text='Click me!', command=click_me)
  button.grid(column=2, row=1)
  button.focus() # Bring focus to textbox as soon as program runs (p. 22)

  # Dropdown menu (p. 24)
  ttk.Label(mighty, text="Choose a number:").grid(column=1,row=0)
  number = tk.StringVar()
  dropdown = ttk.Combobox(mighty, width=12,textvariable=number)
  dropdown['values'] = (1, 2, 4, 42, 100)
  dropdown.grid(column=1, row=1)
  dropdown.current(0)

  # Checkboxes p. 27
  chVarDis = tk.IntVar()
  check1 = tk.Checkbutton(mighty, text="Disabled", variable=chVarDis, state='disabled')
  check1.select()
  # check1.grid(column=0, row=4,)
  # The `sticky=tk.W` appears to change the margin between the element and the window border
  check1.grid(column=0, row=4, sticky=tk.W)

  chVarUn = tk.IntVar()
  check2 = tk.Checkbutton(mighty, text="Unchecked", variable=chVarUn)
  check2.deselect()
  check2.grid(column=1, row=4, sticky=tk.W)

  chVarEn = tk.IntVar()
  check3 = tk.Checkbutton(mighty, text="Enabled", variable=chVarEn)
  check3.select()
  check3.grid(column=2, row=4, sticky=tk.W)

  # Radio buttons
  Blue, Red, Gold = "Blue", "Red", "Gold"

  def colorize(arg, color):
    arg.configure(background=color)
  
  def radCall():
    radSel = radVar.get()
    if radSel == 1: 
      for item in [win, mighty, rad1, rad2, rad3, check1, check2, check3, button, a_label]:
        colorize(item, Red)
    elif radSel == 2: 
      for item in [win, mighty, rad1, rad2, rad3, check1, check2, check3, button, a_label]:
        colorize(item, Blue)
    else: 
      for item in [win, mighty, rad1, rad2, rad3, check1, check2, check3, button, a_label]:
        colorize(item, Gold)

  radVar = tk.IntVar()
  rad1 = tk.Radiobutton(mighty, text=Red, variable=radVar, value=1, command=radCall)
  rad2 = tk.Radiobutton(mighty, text=Blue, variable=radVar, value=2, command=radCall)
  rad3 = tk.Radiobutton(mighty, text=Gold, variable=radVar, value=3, command=radCall)
  
  # rad1.grid(column=0, row=5)
  # rad2.grid(column=1, row=5)
  # rad3.grid(column=2, row=5)

  rad1.grid(column=0, row=5, sticky=tk.W, columnspan=3)
  rad2.grid(column=1, row=5, sticky=tk.W, columnspan=3)
  rad3.grid(column=2, row=5, sticky=tk.W, columnspan=3)

  # Textbox with scrollbar, p. 32
  textbox = scrolledtext.ScrolledText(mighty, width=30, height=5, wrap = tk.WORD)
  textbox.grid(column=0, columnspan=3)

  # Labels, p. 38
  buttons_frame = ttk.LabelFrame(mighty, text=' Labels in a frame   ')
  buttons_frame.grid(column=1, row=7, padx=10, pady=10) #, columnspan=3)
  ttk.Label(buttons_frame, text='Label1').grid(column=0, row=0, sticky=tk.W)
  ttk.Label(buttons_frame, text='Label2').grid(column=1, row=0, sticky=tk.W)
  ttk.Label(buttons_frame, text='Label3').grid(column=2, row=0, sticky=tk.W)

  # - `winfo_children()` method returns a list of all children, (p. 43)
  # - `grid_configure()` method allows modification of UI elements before 
  #    the main loop displays them
  # for i in buttons_frame.winfo_children():
  #   i.grid_configure(padx=8, pady=4)

  # Adding a menu bar, p. 55-56
  menu_bar = tk.Menu(win)
  win.config(menu=menu_bar)

  file_menu = tk.Menu(menu_bar)
  file_menu.add_command(label="New")
  menu_bar.add_cascade(label="File", menu=file_menu)

  win.resizable(True, True)
  win.mainloop()

if __name__ == '__main__':
  main()