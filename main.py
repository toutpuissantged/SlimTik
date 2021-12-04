from autoloader import Config , Store , ArgsParse , FileInterface , Index ,Tk , TabContronller
from typing import TypedDict
class Props(TypedDict):
    root : Tk
    textarea : str
    Store : Store
    Tabs : str
    CurrentActiveTabIndice : int
    Views : dict
    Info : Config

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry(Config.AppInfo['AppScreen'])
        self.title(Config.AppInfo['AppName'])
        self.resizable(False,False)
        self.configure(background=Config.Design['Color']['Background'])
        self.NewStore= Store(1)
        self.props : Props = {
            'root':self,
            'textarea':[],
            'Store':self.NewStore,
            'Tabs':'',
            'CurrentActiveTabIndice':0,
            'Views':{},
            'Info':Config
        }

        FileInt=FileInterface(self.props)
        tab=TabContronller(props=self.props)
        self.props['Tabs']=tab

        Index(props=self.props).main()

        ArgsParse.parse(props=self.props)


if __name__ == "__main__":
    app = App()
    app.mainloop()
