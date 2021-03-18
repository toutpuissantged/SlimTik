from autoloader import *

class EditMenu(FileMenu):

    def __init__(self,props):
        self.props=props
        self.windows=self.props['Views']['windows']    

    def shortcut(self):
        self.undo="Ctrl+Z" 

    def monted(self):
        root=self.windows
        Tab=self.props['Tabs']
        NavBarFrame=Frame(root)
        menu = Menu(NavBarFrame)
        EditBox = Menu(menu)
        self.shortcut()
        Tabnum=0
        EditBox.add_command(label='Undo',command=lambda:FileInt.newfile(),accelerator=self.undo)
        EditBox.add_command(label='Redo',command=lambda:FileInt.openfile(),accelerator="Ctrl+Y")
        EditBox.add_command(label='Cut',command=lambda:FileInt.savefile(),accelerator="Ctrl+X")
        EditBox.add_command(label='Copy',command=lambda:FileInt.savefileas(),accelerator="Ctrl+C")
        EditBox.add_command(label='Paste',command=lambda:Tab.Delete(FileInt.getActiveTab()),accelerator="Ctrl+V")
        menu.add_cascade(label='Edit', menu=EditBox)

        #EditBox.bind("<Control-N>",lambda:FileInt.newfile())
        
        return menu