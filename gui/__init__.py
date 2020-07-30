from tkinter import *
from Resources.cut_paste_rename import list_files
from gui.users import users
from String_match.partial_ratio import *
import json
basePATH = 'D:\\czyFile'
ddddict = dict()



def CallOn(event):
    problemListBox.get(problemListBox.curselection())
    path = problemPathList[problemListBox.curselection()[0]]
    print(path)
    kkkkey = path.split('\\')[2].split('_')[0]
    jsonParser = JsonParser(jsonData=json.loads(open(path + '\\testCases.json').read()))
    users(path, jsonParser, ddddict.get(kkkkey))


if __name__ == '__main__':
    root = Tk()
    root.title('UCOD')

    with open('..\\Structural_analysis\\result', 'r', encoding='utf8') as ffff:

        key = '67666666'
        while True:
            a = ffff.readline().strip()
            if not a:
                break
            if a.startswith('case_id'):
                a = a[8:]
                key = a
                ddddict[a] = dict()
            else:
                a = a.split()
                ddddict[key][a[0]] = (a[1], a[2])

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
