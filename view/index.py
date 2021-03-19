from autoloader import *

class Index():

    def __init__(self,props):
        self.props=props
        self.props['Views']['windows']=Frame(self.props['root'])

    def main(self):

        root=self.props['root']
        menubar = Menu(root)
        props=self.props
        self.props['Views']['Menu']=menubar
        root.config(menu=menubar)
        
        NavBar=FileMenu(props=props)
        NavBar2=EditMenu(props=props)

        File=NavBar.monted()
        Edit=NavBar2.monted()

        menubar.add_cascade(label='File', menu=File)
        menubar.add_cascade(label='Edit', menu=Edit)

        return 0