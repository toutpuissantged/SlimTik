from autoloader import *

root = Tk()
root.geometry("500x380")
root.title('Editor+')

root.iconphoto(False, PhotoImage(file = 'assets/icon.png'))

NewStore= Store(1)

props={
    'root':root,
    'textarea':[],
    'Store':NewStore,
    'Tabs':'',
    'CurrentActiveTabIndice':0,
    'Views':{}
}

FileInt=FileInterface(props)
tab=TabContronller(props=props)
props['Tabs']=tab

ViewsEntry=Index(props=props)
ViewsEntry.main()

FirstTab=tab.New()

root.mainloop()