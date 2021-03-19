from autoloader import *

class EditMenu(FileMenu):

    def __init__(self,props):
        self.props=props
        self.windows=self.props['Views']['windows']    
        self.MyMenu=self.props['Views']['Menu'] 

        self.shortcut()

    def shortcut(self):
        self.Undo="Ctrl+Z" 
        self.Redo="Ctrl+Y"
        self.Cut="Ctrl+X"
        self.Copy="Ctrl+C"
        self.Paste="Ctrl+V"

    def monted(self):
        root=self.windows
        Tab=self.props['Tabs']
        NavBarFrame=Frame(root)
        menu = Menu(NavBarFrame)
        EditBox = Menu(menu)
        
        Tabnum=0
        EditBox.add_command(label='Undo',command=lambda:FileInt.newfile(),accelerator=self.Undo)
        EditBox.add_command(label='Redo',command=lambda:FileInt.openfile(),accelerator=self.Redo)
        EditBox.add_command(label='Cut',command=lambda:FileInt.savefile(),accelerator=self.Cut)
        EditBox.add_command(label='Copy',command=lambda:FileInt.savefileas(),accelerator=self.Copy)
        EditBox.add_command(label='Paste',command=lambda:Tab.Delete(FileInt.getActiveTab()),accelerator=self.Paste)

        return EditBox