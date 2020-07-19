from tkinter import *
import os
from Resources.cut_paste_rename import list_files

size = '1440x810'


class users:
    def __init__(self, path):
        self.root = Tk()
        self.panedWindow = PanedWindow(self.root)
        self.panedWindow.pack(side='left')
        self.basePATH = path
        self.root.title(path)
        self.root.geometry(size)
        self.userListBox = Listbox(self.panedWindow, width=18, height=30)
        self.userPathList = [item for item in list_files(path)
                        if item.endswith(".py") and not item.endswith('answer.py')]
        [self.userListBox.insert(self.userListBox.size(), str(item).split('\\')[3][5:-3])
         for item in self.userPathList]

        self.userListBox.bind('<Double-Button-1>', self.userCallOn)
        self.userListBox.pack()

        true_answer_button = Button(self.panedWindow, text='answer', command=self.answer)
        true_answer_button.pack()
        readmeButton = Button(self.panedWindow, text='readme', command=self.readme)
        readmeButton.pack()
        test_case_button = Button(self.panedWindow, text='test-cases', command=self.testCase)
        test_case_button.pack()

        self.textView = Text(self.root, width=150, height=54, state='disabled')

        self.textView.pack()

    def userCallOn(self, event):
        path = self.userPathList[self.userListBox.curselection()[0]]
        self.refreshTextByPath(path)
        pass

    def refreshTextByFile(self, file):
        path = self.basePATH + '\\' + file
        self.refreshTextByPath(path)
        pass

    def refreshTextByPath(self, path):
        textStr = open(path, encoding='utf8').read()
        self.refreshTextByString(textStr)
        pass

    def refreshTextByString(self, string):
        self.textView.configure(state='normal')
        self.textView.delete(0.0, END)
        self.textView.insert(0.0, string)
        self.textView.configure(state='disabled')
        pass

    def answer(self, ):
        self.refreshTextByFile('answer.py')
        pass

    def readme(self):
        self.refreshTextByFile('readme.md')
        pass

    def testCase(self):
        self.refreshTextByFile('testCases.json')
        pass
