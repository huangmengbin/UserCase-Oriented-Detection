from tkinter import *
from String_match.format import code_format
from Resources.cut_paste_rename import list_files
from String_match.extract_data import extracter
size = '1440x810'


class users:
    def __init__(self, path):
        self.root = Tk()
        self.panedWindow = PanedWindow(self.root)
        self.panedWindow.pack(side='left')
        # 左边那个栏
        self.code_extracter = extracter('')
        self.basePATH = path
        self.root.title(path)
        self.root.geometry(size)

        self.extractButton = Button(self.panedWindow, text='数据提取', command=self.extractAction, state='disabled')
        self.extractButton.pack()
        self.userListBox = Listbox(self.panedWindow, width=18, height=30)
        self.userPathList = [item for item in list_files(path)
                        if item.endswith(".py") and not item.endswith('answer.py')]
        [self.userListBox.insert(self.userListBox.size(), str(item).split('\\')[3][5:-3])
         for item in self.userPathList]
        self.userListBox.bind('<Double-Button-1>', self.userCallOn)
        self.userListBox.pack()
        self.true_answer_button = Button(self.panedWindow, text='answer', command=self.answerAction)
        self.true_answer_button.pack()
        self.readmeButton = Button(self.panedWindow, text='readme', command=self.readmeAction)
        self.readmeButton.pack()
        self.test_case_button = Button(self.panedWindow, text='test-cases', command=self.testCaseAction)
        self.test_case_button.pack()
        self.textView = Text(self.root, width=150, height=54, state='disabled')
        self.textView.pack()

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

    def gotoUserState(self):
        self.extractButton.configure(state='normal')

    def exitUserState(self):
        self.extractButton.configure(state='disabled')

    def userCallOn(self, event):
        my_path = self.userPathList[self.userListBox.curselection()[0]]
        code = open(my_path, encoding='utf8').read()
        code = code_format(code)
        self.code_extracter = extracter(code)
        self.refreshTextByString(code)
        self.gotoUserState()
        pass

    def answerAction(self, ):
        self.refreshTextByFile('answer.py')
        self.exitUserState()
        pass

    def readmeAction(self):
        self.refreshTextByFile('readme.md')
        self.exitUserState()
        pass

    def testCaseAction(self):
        self.refreshTextByFile('testCases.json')
        self.exitUserState()
        pass

    def extractAction(self):
        self.refreshTextByString(self.code_extracter.afterExtractCode)
        self.exitUserState()
        pass