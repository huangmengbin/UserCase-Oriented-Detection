from tkinter import ttk
from tkinter import *
from Resources.cut_paste_rename import list_files
from gui.users import users

basePATH = 'D:\\czyFile'



def CallOn(event):
    problemListBox.get(problemListBox.curselection())
    users(problemPathList[problemListBox.curselection()[0]])


if __name__ == '__main__':
    root = Tk()
    root.title('UCOD')

    #following lines are used for UI size set
    curWidth=root.winfo_width()
    curHeight=root.winfo_height()
    scnWidth,scnHeight=root.maxsize()
    size='+%d+%d' %((scnHeight-curWidth)/2,(scnHeight-curHeight)/3)
    root.geometry(size)

    problemListBox = Listbox(root, width=100, height=40)


    problemPathList = list_files(basePATH)
    [problemListBox.insert(problemListBox.size(), str(item).split('\\')[2])
     for item in problemPathList]
    problemListBox.bind('<Double-Button-1>', CallOn)
    problemListBox.pack(side=LEFT,fill=BOTH)

    root.mainloop()
