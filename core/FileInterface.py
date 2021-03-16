from autoloader import *

class FileInterface():
    
    def __init__(self,props):
       self.props=props

    def newfile(self):
        self.filefactory(data='')

    def openfile(self):
        '''  openfile in binarie mode and return content '''
        props=self.props
        filedir=filedialog.askopenfile(title="select folder")
        try : temp1=filedir.name 
        except:  return 0
        ff=open(filedir.name,'rb')
        data=ff.read()
        ff.close()
        props['textarea'].insert(INSERT,data)
        props['Store'].set_data(filedir.name)
        return 0

    def savefileas(self):
        '''    save file in new directory   '''
        data=self.props['textarea'].get(1.0,END)
        self.filefactory(data=data)

    def savefile(self):
        '''    save file in new directory   '''
        props=self.props
        filedir=props['Store'].get_data()
        if (len(filedir)<1): return 0
        print(filedir)
        data=props['textarea'].get(1.0,END)
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