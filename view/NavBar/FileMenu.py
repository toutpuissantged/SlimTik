from autoloader import *

class FileMenu():

    def __init__(self,windows,props):
        self.windows=windows
        self.props=props
        self.FileInt=FileInterface(self.props)
        self.props['FileInt']=self.FileInt

    def monted(self):
        FileInt=self.FileInt
        root=self.windows
        Tab=self.props['Tabs']
        NavBarFrame=Frame(root)
        menu = Menu(NavBarFrame)
        FileBox = Menu(menu)
        Tabnum=0
        FileBox.add_command(label='New File',command=lambda:FileInt.newfile(),accelerator="Ctrl+N")
        FileBox.add_command(label='Open File',command=lambda:FileInt.openfile(),accelerator="Ctrl+S")
        FileBox.add_command(label='Save',command=lambda:FileInt.savefile(),accelerator="Ctrl+Shift+S")
        FileBox.add_command(label='Save As',command=lambda:FileInt.savefileas(),accelerator="Ctrl+Q")
        FileBox.add_command(label='close file',command=lambda:Tab.Delete(FileInt.getActiveTab()),accelerator="Ctrl+E")
        FileBox.add_command(label='Exit',command=root.quit)
        menu.add_cascade(label='File', menu=FileBox)

        FileBox.bind("<Control-N>",lambda:FileInt.newfile())
        
        return menu