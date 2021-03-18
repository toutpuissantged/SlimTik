from autoloader import *

class Index():

    def __init__(self,props):
        self.props=props
        self.props['Views']['windows']=Frame(self.props['root'])

    def main(self):
        root=self.props['root']
        props=self.props
        
        NavBar=FileMenu(windows=root,props=props)
        NavBar2=EditMenu(props=props)

        menu=NavBar.monted()
        menu2=NavBar2.monted()

        root.config(menu=menu)
        root.config(menu=menu2)
        