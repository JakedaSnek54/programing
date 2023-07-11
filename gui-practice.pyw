import tkinter as tk
from tkinter import messagebox
class GUI:
    def __init__(self):
        self.root =tk.Tk()
        self.Menu =tk.Menu(self.root)

        self.fileMenu=tk.Menu(self.Menu, tearoff=0)
        self.fileMenu.add_command(label="Exit", command=self.on_closing)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label='Exit without saving', command= exit)
        self.Menu.add_cascade(menu=self.fileMenu, label="File")
        self.root.config(menu=self.Menu)
        
        self.actionmenu =tk.Menu(self.Menu, tearoff=0)
        self.actionmenu.add_command(label='Show Messgae', command= self.ShowMes)
        self.Menu.add_cascade(menu=self.actionmenu, label="Action")


        self.label = tk.Label(self.root, text='Your Message', font=('Arial',18))
        
        self.label.pack(padx=10, pady=10)
        self.textbox = tk.Text(self.root, height=5, font=('arial',18))
        self.textbox.pack(padx=10,pady=10)
        self.textbox.bind("<KeyPress>", self.Shortcut)
        self.button = tk.Button(self.root, text="Enter", font=("Arial", 18),command=self.ShowMes)
        self.button.pack(padx=10,pady=10)
        self.clearbutton = tk.Button(self.root, text="Clear", font=('Arial', 18),command= self.Clear)
        self.clearbutton.pack(padx=10, pady= 10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()





    def ShowMes(self):
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))
    def Shortcut(self, event):
        if event.keysym == "Return":
            self.ShowMes()
    def on_closing(self):
        if messagebox.askyesno(title="Quit", message='Do you really want to quit'):
            self.root.destroy()
    def Clear(self):
        self.textbox.delete('1.0', tk.END)
GUI()
            