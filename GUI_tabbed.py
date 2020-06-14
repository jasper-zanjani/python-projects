import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

def main():
  def _quit():
    window.quit()
    window.destroy()
    exit()
  def click_me():
    button.configure(text=f"Hello {name.get()}")
    button.configure(state='disabled') # Disable button after it is pressed, p. 23

    # Method chaining throws an `AtributeError`
    # a_label.configure(foreground='red').configure(text='A Red Label')
    a_label.configure(foreground='red',text='Button is clicked!')
  def radCall():
    radSel = radVar.get()
    if radSel == 1: mighty2.configure(text='Gold')
    elif radSel == 2: mighty2.configure(text='Red')
    else: mighty2.configure(text='Blue')

  def _msgBox():
    messagebox.showinfo('Python Message Info Box', 'A Python GUIcreated using `tkinter`\nThe year is 2020.')
  window = tk.Tk()
  window.title("Python GUI")

  # Adding a menu bar, p. 55-56
  menu_bar = tk.Menu(window)
  window.config(menu=menu_bar)
  
  file_menu = tk.Menu(menu_bar, tearoff=0) 
  file_menu.add_command(label="New")
  file_menu.add_separator() # p. 58
  file_menu.add_command(label="Exit", command=_quit) # p. 57
  menu_bar.add_cascade(label="File", menu=file_menu)

  help_menu = tk.Menu(menu_bar, tearoff=0) 
  menu_bar.add_cascade(label="Help", menu=help_menu)
  help_menu.add_command(label="About", command=_msgBox)

  # Tab controls, p. 63
  tabControl = ttk.Notebook(window)
  
  tab1 = ttk.Frame(tabControl)
  tabControl.add(tab1, text='Tab 1')

  mighty = ttk.LabelFrame(tab1, text=" Mighty Python") # p. 64
  mighty.grid(column = 0, row = 0, padx=8, pady=4)

  a_label = ttk.Label(mighty, text="Enter a name:")
  a_label.grid(column = 0, row = 0, sticky=(tk.W, tk.E))

  name = tk.StringVar()
  textbox = ttk.Entry(mighty, width=12, textvariable=name)
  textbox.grid(column=0, row=1, sticky='WE')

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

  tab2 = ttk.Frame(tabControl)
  tabControl.add(tab2, text='Tab 2')

  mighty2 = ttk.LabelFrame(tab2, text='The Snake')
  mighty2.grid(column=0,row=0,padx=8,pady=4)

  # Labels, p. 38
  buttons_frame = ttk.LabelFrame(mighty2, text=' Labels in a frame   ')
  buttons_frame.grid(column=1, row=7, padx=10, pady=10) #, columnspan=3)
  ttk.Label(buttons_frame, text='Label1').grid(column=0, row=0, sticky=tk.W)
  ttk.Label(buttons_frame, text='Label2').grid(column=1, row=0, sticky=tk.W)
  ttk.Label(buttons_frame, text='Label3').grid(column=2, row=0, sticky=tk.W)


  # Radio buttons
  Blue, Red, Gold = "Blue", "Red", "Gold"

  radVar = tk.IntVar()
  rad1 = tk.Radiobutton(mighty2, text=Red, variable=radVar, value=1, command=radCall)
  rad2 = tk.Radiobutton(mighty2, text=Blue, variable=radVar, value=2, command=radCall)
  rad3 = tk.Radiobutton(mighty2, text=Gold, variable=radVar, value=3, command=radCall)

  rad1.grid(column=0, row=5, sticky=tk.W, columnspan=3)
  rad2.grid(column=1, row=5, sticky=tk.W, columnspan=3)
  rad3.grid(column=2, row=5, sticky=tk.W, columnspan=3)

  # Checkboxes
  chVarDis = tk.IntVar()
  check1 = tk.Checkbutton(mighty2, text="Disabled", variable=chVarDis, state='disabled')
  check1.select()
  check1.grid(column=0, row=4, sticky=tk.W)

  chVarUn = tk.IntVar()
  check2 = tk.Checkbutton(mighty2, text="Unchecked", variable=chVarUn)
  check2.deselect()
  check2.grid(column=1, row=4, sticky=tk.W)

  chVarEn = tk.IntVar()
  check3 = tk.Checkbutton(mighty2, text="Enabled", variable=chVarEn)
  check3.select()
  check3.grid(column=2, row=4, sticky=tk.W)

  # Textbox with scrollbar, p. 32
  textbox = scrolledtext.ScrolledText(mighty, width=30, height=5, wrap = tk.WORD)
  textbox.grid(column=0, columnspan=3)

  tabControl.pack(expand=1, fill='both')

  window.mainloop()

if __name__ == '__main__':
  main()