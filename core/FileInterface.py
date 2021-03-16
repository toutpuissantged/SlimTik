from autoloader import *

class FileInterface():
    
    def __init__(self,props):
       self.props=props
       #self.TabNum=TabNum
       #self.get_TabState= self.props['Store'].get_TabState
       #self.set_TabState=self.props['Store'].set_TabState
       self.TabState=self.props['Store'].TabState

    def newfile(self):
        
        self.props['Tabs'].New()

    def openfile(self,Tabnum=0):
        '''  openfile in binarie mode and return content '''
        props=self.props   
        
        filedir=filedialog.askopenfile(title="select folder")
        try : temp1=filedir.name 
        except:  return 0
        ff=open(filedir.name,'rb')
        data=ff.read()
        ff.close()
        #props['textarea'].insert(INSERT,data)
        #props['Store'].set_data(filedir.name)
        self.props['Tabs'].New(title=temp1)
        print(self.TabState)
        curTab=self.TabState[len(self.TabState)-1]
        curTab['textarea'].insert(INSERT,data)
        curTab['fildir']=filedir.name
        props['Store'].set_data(filedir.name)
        
        return 0

    def savefileas(self,Tabnum=0):
        '''    save file in new directory   '''
        data=self.TabState[Tabnum]['textarea'].get(1.0,END)
        self.filefactory(data=data)

    def savefile(self,Tabnum=0):
        '''    save file in new directory   '''
        props=self.props
        curTab=self.TabState[Tabnum]['textarea']
        filedir=props['Store'].get_data()
        if (len(filedir)<1): return 0
        print(filedir)
        data=self.TabState[Tabnum]['textarea'].get(1.0,END)
        ff=open(filedir,'w');ff.write(data);ff.close()
        print('done')
        return 0

   
    def filefactory(self,data=''):
        filedir=filedialog.asksaveasfilename(title="choose destination")
        if (len(filedir)<1): return 0
        print(filedir)
        ff=open(filedir,'w');ff.write(data);ff.close()
        self.props['Store'].set_data(filedir)
        print('done')
        return 0