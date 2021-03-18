from autoloader import *

root = Tk()
root.geometry("500x380")
root.title('Editor+')

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
'''NavBar=FileMenu(windows=root,props=props)
menu=NavBar.monted()
root.config(menu=menu)'''


tab.New()

root.mainloop()