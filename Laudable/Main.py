import tkinter as tk
from tkinter import ttk

def main():
    win = tk.Tk()
    win.title("ACME Sales Corp ")
    page = ttk.LabelFrame(win, text="ACME Sales Corp")
    page.grid(column=0, row=0)
    first_name = ''
    last_name = ''
    email = ''

    label_fn = ttk.Label(page, text="First name:")
    label_fn.grid(column=0, row=0, sticky=(tk.W, tk.E))
    txtbx_fn = ttk.Entry(page, textvariable=first_name)
    txtbx_fn.grid(column=1, row=0)
    
    label_ln = ttk.Label(page, text="Last name:")
    label_ln.grid(column=0, row=1, sticky=(tk.W, tk.E))
    txtbx_ln = ttk.Entry(page, textvariable=last_name)
    txtbx_ln.grid(column=1, row=1)

    label_email = ttk.Label(page, text="Last name:")
    label_email.grid(column=0, row=2, sticky=(tk.W, tk.E))
    txtbx_email = ttk.Entry(page, textvariable=email)
    txtbx_email.grid(column=1, row=2)

    win.resizable(False,False)
    win.mainloop()

if __name__ == '__main__':
    main()
