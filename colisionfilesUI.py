from Tkinter import *
from PIL import Image  
import tkFileDialog, os
from colisionFiles import *
  
rootPath = ()
tree = AVLTree()


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
    global tree

    selectPath.pack_forget() 
    searching.pack()

    tree.insertPath(rootPath)

    labelResult2.config(text=str(len(tree.getColisionList())))
    searching.pack_forget()
    viewResults.pack()
    if (len(tree.getColisionList())>0):
        optionsResult.pack()

def finish():
    generating.pack_forget() 
    done.pack()

def generateTxt():
    viewResults.pack_forget()
    generating.pack()
    txt = generateStrTxt(tree.getColisionList().items());
    f = open('colisions.txt', 'w')
    f.write(txt)
    f.close()
    finish()

def generateHtml():
    viewResults.pack_forget()

    generating.pack()

    html = generateStrHTML(tree.getColisionList().items());
    f = open('colisions.html', 'w')
    f.write(html)
    f.close()
    finish()

def generateStrTxt(colisionItems):
    txt = """"""
    for key, c in colisionItems:
        txt+=str(c) + "\n"
    return txt

def generateStrHTML(colisionItems):
    html = """
    <html>
    <head>
	    <title>Colision Galery</title>
        <style>
            body{
	            background-color: grey;
            }

            #galery {
            border: 1px solid #EAEAEA;
            border-radius: 25px;
            padding: 20px;
            padding-bottom: 0;
            background: #0099CC;
            width: 940px;
            margin: auto;
            }

            #imgBig {
            border: 1px solid #F2F2F2;
            border-radius: 25px;
            width: 940px;
            height: 300px;
            }

            #galery_min{
	            display: table;
                margin: 0 auto;
            }

            .img_min {
            width:  60px;
            height:  60px;
            border-radius: 10px;
            float: left;
            cursor: pointer;
            padding: 5px;
            margin: 10px 5px;
            }

            #resume {
            border: 1px solid #EAEAEA;

            border-radius: 25px;
            padding: 20px;
            padding-bottom: 0;
            background: #0099CC;
            width: 940px;

            margin: auto;
            }
        </style>
    </head>
    <body>
          <div id="galery">
            
            <div id="principal_galery">
    """
    for key, c in colisionItems:
        html+="""<img id="imgBig"src='"""+ c.path[0] + """'>"""

        break
    html+="""
            </div>
            <div id="galery_min">
          """
    for key, c in colisionItems:
        html+="""<img class="img_min" src='""" + c.path[0] +"""'onclick="{
                document.getElementById('imgBig').src='""" + c.path[0] + """'
                document.getElementById('hash').innerHTML = '"""+ c.md5 +"""'
                document.getElementById('colisions').innerHTML = '"""+ str(c.count) +"""'
                paths = document.getElementById('paths');
                while (paths.firstChild) {
                    paths.removeChild(paths.firstChild);
                }
                """
        for path in c.path:
            html+="""
            label = document.createElement('label');
            label.innerHTML ='""" +path +"""'; 
            paths.appendChild(label);
            br = document.createElement('br');
            paths.appendChild(br);
            """
        html+="""}">"""
    html+="""
             </div>
          </div>
        <div id ="resume">"""
    for key, c in colisionItems:
        html+="""<label id="hashlabel">Hash</label>
                <label id="hash">"""+ c.md5 + """</label>
                <br></br>
                <label id="colisionslabel">Colisions</label>
                <label id="colisions">""" + str(c.count) +"""</label>
                <br></br>
                <label id="pathslabel">Paths</label>
                <div id="paths">
                """
        for path in c.path:
            html+="""<label>"""+ path + """</label><br>"""
        html+="""</div>"""
                
        break
    html+="""
        </div>

    </body>
    </html>
    """
    return html

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

    done = Frame(root)
    """pack when finisk generate"""
    labelDone = Label(done, text = "Done")
    labelDone.pack()


    root.mainloop() 


