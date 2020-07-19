from tkinter import *
import os
from Resources.cut_paste_rename import list_files

size = '1440x810'


class users:
    def __init__(self, path):
        self.root = Tk()
        self.panedWindow = PanedWindow(self.root)
        self.panedWindow.pack(side='left')
        self.path = path
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
        file = self.userPathList[self.userListBox.curselection()[0]].split('\\')[-1]
        self.refresh_text(file)
        pass

    def refresh_text(self, file):
        textStr = open(self.path + '\\' + file, encoding='utf8').read()
        self.textView.configure(state='normal')
        self.textView.delete(0.0, END)
        self.textView.insert(0.0, textStr)
        self.textView.configure(state='disabled')
        pass

    def answer(self, ):
        self.refresh_text('answer.py')
        pass

    def readme(self):
        self.refresh_text('readme.md')
        pass

    def testCase(self):
        self.refresh_text('testCases.json')
        pass
