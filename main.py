from autoloader import *


root = Tk()
root.geometry("500x380")
root.title('editorplus')
global btn1,textarea
textdata=StringVar()

textarea=Text(root,border=0,fg="black",bg="white",width=60,height=20)
textarea.grid(row=0,column=0,padx=10,pady=10)


btn_Fr=Frame(root)
btn_Fr.grid()


def openfile():
    global btn1,textarea
    filedir2=filedialog.askopenfile(title="select folder")
    if filedir2.name=='':
        return 0
    print('filedir=')
    print(filedir2.name)
    ff=open(filedir2.name,'rb')
    data=ff.read()
    ff.close()
    print(data)
    textarea.insert(INSERT,data)


btn1=Button(btn_Fr,text="save").grid(row=1,column=0)
btn1=Button(btn_Fr,text="save as").grid(row=1,column=1)
btn1=Button(btn_Fr,text="open",command=openfile).grid(row=1,column=2)

root.mainloop()