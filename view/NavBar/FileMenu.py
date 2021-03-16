from autoloader import *

class FileMenu():

    def __init__(self,windows,props):
        self.windows=windows
        self.props=props

    def monted(self):

        root=self.windows
        FileInt=FileInterface(self.props)
        NavBarFrame=Frame(root)
        menu = Menu(NavBarFrame)
        new_item = Menu(menu)
        Tabnum=0
        new_item.add_command(label='New File',command=lambda:FileInt.newfile())
        new_item.add_command(label='Open File',command=lambda:FileInt.openfile(Tabnum=Tabnum))
        new_item.add_command(label='Save',command=lambda:FileInt.savefile(Tabnum=Tabnum))
        new_item.add_command(label='Save As',command=lambda:FileInt.savefileas(Tabnum=Tabnum))
        new_item.add_command(label='Exit',command=root.quit)
        menu.add_cascade(label='File', menu=new_item)
        
        return menu