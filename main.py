from autoloader import *

root = Tk()
root.geometry("500x380")
root.title('Editor+')

textarea=scrolledtext.ScrolledText(root,border=0,fg="black",bg="white",width=60,height=20)
textarea.grid(row=0,column=0,padx=10,pady=10)

NewStore= Store(1)

props={
    'root':root,
    'textarea':textarea,
    'Store':NewStore,
}
FileInt=FileInterface(props)

NavBar=FileMenu(windows=root,props=props)
menu=NavBar.monted()
root.config(menu=menu)

#test zone
tab_control = Notebook(root)

tab1 = Frame(tab_control)

tab2 = Frame(tab_control)

tab_control.add(tab1, text='First')

tab_control.add(tab2, text='Second')

lbl1 = Label(tab1, text= 'label1')

lbl1.grid(column=0, row=0)

lbl2 = Label(tab2, text= 'label2')

lbl2.grid(column=0, row=0)

tab_control.grid()
#endof test zone

#print(props['data'])

root.mainloop()