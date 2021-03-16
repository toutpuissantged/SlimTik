from autoloader import *
from tkinter import scrolledtext

class TabContronller(object):

    def __init__(self,props ):
        self.props=props
        self.tab_control = Notebook(props['root'])
        self.tabLen=0
        self.curentTab=1

    def New(self):
        self.tabLen+=1
        tabNum=self.tabLen
        self.tab2=Frame(self.tab_control)
        titre = ' Untitled-'+str(tabNum)
        props=self.props
        self.tab_control.add(self.tab2, text=titre)
        textarea = scrolledtext.ScrolledText(self.tab2,border=0,fg="black",bg="white",width=60,height=20)
        textarea.grid(column=0, row=0)
        self.tab_control.grid()
        props['Store'].set_TabState(newdata=textarea,method='append')
        return textarea