from autoloader import *

class FileMenu():

    def __init__(self,windows,props):
        self.windows=windows
        self.props=props
        pass

    def monted(self):

        root=self.windows
        FileInt=FileInterface(self.props)
        NavBarFrame=Frame(root)
        menu = Menu(NavBarFrame)
        new_item = Menu(menu)
        new_item.add_command(label='New File',command=FileInt.newfile)
        new_item.add_command(label='Open File',command=FileInt.openfile)
        new_item.add_command(label='Save',command=FileInt.savefile)
        new_item.add_command(label='Save As',command=FileInt.savefileas)
        new_item.add_command(label='Exit',command=root.quit)
        menu.add_cascade(label='File', menu=new_item)
        
        return menu