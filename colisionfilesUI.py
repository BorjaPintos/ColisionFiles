from Tkinter import *
from PIL import Image  
import tkFileDialog, os
from colisionFiles import *
  
rootPath = ()


def checkValidateDir():
    global rootPath

    if (os.path.isdir(rootPath)):
        buttonSearch.config(state=ACTIVE)
    else:
        buttonSearch.config(state=DISABLED)

def entryChange(*args):
    global rootPath
    rootPath = entryPath.get()
    checkValidateDir()


def askdirectory():
    global rootPath
    dir_opt = options = {}
    options['mustexist'] = False
    options['parent'] = root
    options['title'] = 'Choose a directory'

    rootPath = tkFileDialog.askdirectory(**dir_opt)

    if (rootPath!='' and rootPath!=()):
        entryPath.delete(0, END)
        entryPath.insert(0, rootPath)    

    
def search():
    global rootPath

    selectPath.pack_forget() 
    searching.pack()

    tree = AVLTree()
    tree.insertPath(rootPath)

    labelResult2.config(text=str(len(tree.getColisionList())))
    searching.pack_forget()
    viewResults.pack()
    if (len(tree.getColisionList())>0):
        optionsResult.pack()


def generateTxt():
    viewResults.pack_forget()
    generating.pack()
    """
    for key, c in tree.getColisionList().items():
        print c
    """

def generateHtml():
    viewResults.pack_forget()
    generating.pack()
    """
    for key, c in tree.getColisionList().items():
        print c
    """

if __name__=='__main__':


    root = Tk()
    root.wm_title("Colision Files")
    root.minsize(width=300, height=20)  
    selectPath = Frame(root)  
    selectPath.pack()  
      
    group = LabelFrame(selectPath, text="", height=320, width=320)
    group.pack(side=TOP)
 
    folderIcon = PhotoImage(file='./folder.gif')
    entryPathVar = StringVar()
    entryPathVar.trace("w", entryChange)
    entryPath = Entry(group, textvariable=entryPathVar) 
    entryPath.pack(side=RIGHT) 
    buttonFolder = Button(group, image=folderIcon, command=askdirectory)  
    buttonFolder.pack(side=LEFT) 
    searchIcon = PhotoImage(file='./search.gif')
    buttonSearch = Button(selectPath, image=searchIcon, state=DISABLED, command=search)
    buttonSearch.pack(side=BOTTOM)

    searching = Frame(root)
    """pack when click in search"""
    labelSearching = Label(searching, text = "Searching...")
    labelSearching.pack()
    
    viewResults = Frame(root)
    """pack when finish search"""
    labelsResult = Frame(viewResults)
    labelsResult.pack()
    labelResult1 = Label(labelsResult, text = "Found")
    labelResult1.pack(side=LEFT)
    labelResult2 = Label(labelsResult)
    labelResult2.pack(side=LEFT)
    labelResult3 = Label(labelsResult, text = "identical files")
    labelResult3.pack(side=RIGHT)

    optionsResult = LabelFrame(viewResults)
    buttonTxt = Button(optionsResult, text="Generate txt", command=generateTxt)
    buttonTxt.pack(side=TOP)
    labelOption = Label(optionsResult, text = "or")
    labelOption.pack()
    buttonHtml = Button(optionsResult, text="Generate HTML (for images)", command=generateHtml)
    buttonHtml.pack(side=BOTTOM)

    generating = Frame(root)
    """pack when click in generate"""
    labelGenerating = Label(generating, text = "Generating...")
    labelGenerating.pack()


    root.mainloop() 


