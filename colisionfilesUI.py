from Tkinter import *  
import tkFileDialog, os
from colisionFiles import *
  
rootPath = ()


def checkValidateDir():
    global rootPath

    if (os.path.isdir(rootPath)):
        buttonF.config(state=ACTIVE)
    else:
        buttonF.config(state=DISABLED)

def entryChange(*args):
    global rootPath
    rootPath = entry.get()
    checkValidateDir()


def askdirectory():
    global rootPath
    dir_opt = options = {}
    options['mustexist'] = False
    options['parent'] = root
    options['title'] = 'Choose a directory'

    rootPath = tkFileDialog.askdirectory(**dir_opt)

    if (rootPath!='' and rootPath!=()):
        entry.delete(0, END)
        entry.insert(0, rootPath)    

    
def search():
    global rootPath

    """SPINER CARGANDO"""

    tree = AVLTree()
    tree.insertPath(rootPath)

    """GENERAR HTML pasando colisionList"""

    for key, c in tree.getColisionList().items():
        print c


if __name__=='__main__':


    root = Tk()  
    frame = Frame(root)  
    frame.pack()  
      
    group = LabelFrame(frame, text="", height=320, width=320)
    group.pack(side=TOP)
 
    folderIcon = PhotoImage(file='./folder.gif')
    entryVar = StringVar()
    entryVar.trace("w", entryChange)
    entry = Entry(group, textvariable=entryVar) 
    button = Button(group, image=folderIcon, command=askdirectory)  
      
    button.pack(side=LEFT) 
    entry.pack(side=RIGHT)  
 
    searchIcon = PhotoImage(file='./search.gif')
    buttonF = Button(frame, image=searchIcon, state=DISABLED, command=search)
    buttonF.pack(side=BOTTOM)
      
    root.mainloop() 
