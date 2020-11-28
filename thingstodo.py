import tkinter as tk

Root = tk.Tk()
Root.title("Registration form")
Root. configure(bg='#ff1234')

mytodolist= tk.Label(Root, text= "My Todo List:")
enterkeep= tk.Entry(Root)
showsithere= tk.Listbox(Root)


def deleting():
    showsithere.delete(showsithere.curselection())

def adding():
    one= enterkeep.get()
    showsithere.insert("end", one)



Additem=tk.Button(Root, text= "Add Item", command=adding)
Deleteitem=tk.Button(Root, text="Delete Item", command=deleting)



mytodolist.grid(row= 0, column= 0)
Additem.grid(row= 1, column= 2)
Deleteitem.grid(row= 5, column= 2)
enterkeep.grid(row=1, column= 0)
showsithere.grid(row= 5, column= 0)

Root.mainloop()