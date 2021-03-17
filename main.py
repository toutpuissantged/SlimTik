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
    'CurrentActiveTabIndice':0
}

FileInt=FileInterface(props)
tab=TabContronller(props=props)

props['Tabs']=tab

NavBar=FileMenu(windows=root,props=props)
menu=NavBar.monted()
root.config(menu=menu)

#test zone

tab.New()
tab.New()

#endof test zone

#print(props['data'])

root.mainloop()