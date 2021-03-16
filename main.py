from autoloader import *

root = Tk()
root.geometry("500x380")
root.title('Editor+')

NewStore= Store(1)

props={
    'root':root,
    'textarea':[],
    'Store':NewStore,
    'Tabs':''
}
FileInt=FileInterface(props)

NavBar=FileMenu(windows=root,props=props)
menu=NavBar.monted()
root.config(menu=menu)

#test zone
tab=TabContronller(props=props)
tab.New()
tab.New()
props['Tabs']=tab

#endof test zone

#print(props['data'])

root.mainloop()