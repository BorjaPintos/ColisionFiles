import Tkinter, Tkconstants, tkFileDialog

class TkFileDialogExample(Tkinter.Frame):

    def __init__(self, root):

        Tkinter.Frame.__init__(self, root)

        # options for buttons
        button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}

        Tkinter.Button(self, text='Choose a directory', command=self.askdirectory).pack(**button_opt)

        # This is only available on the Macintosh, and only when Navigation Services are installed.
        #options['message'] = 'message'

        # if you use the multiple file version of the module functions this option is set automatically.
        #options['multiple'] = 1

        # defining options for opening a directory
        self.dir_opt = options = {}
        options['mustexist'] = True
        options['parent'] = root
        options['title'] = 'Choose a directory'



    def askdirectory(self):

        """Returns a selected directoryname."""

        return tkFileDialog.askdirectory(**self.dir_opt)

if __name__=='__main__':
    root = Tkinter.Tk()
    TkFileDialogExample(root).pack()
    root.mainloop()
