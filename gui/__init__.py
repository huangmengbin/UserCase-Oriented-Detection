import tkinter
from Resources.cut_paste_rename import list_files
from gui.users import users

basePATH = 'D:\\czyFile'
size = '1440x810'


def CallOn(event):
    problemListBox.get(problemListBox.curselection())
    users(problemPathList[problemListBox.curselection()[0]])


if __name__ == '__main__':
    root = tkinter.Tk()
    root.geometry(size)
    problemListBox = tkinter.Listbox(root, width=100, height=40)
    problemPathList = list_files(basePATH)
    [problemListBox.insert(problemListBox.size(), str(item).split('\\')[2])
     for item in problemPathList]
    problemListBox.bind('<Double-Button-1>', CallOn)
    problemListBox.pack()
    root.mainloop()
