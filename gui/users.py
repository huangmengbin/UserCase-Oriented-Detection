from tkinter import *
from tkinter import  ttk
from Resources.cut_paste_rename import list_files
from String_match.extract_data import extracter
import numpy as np
import matplotlib.pyplot as plt
size = '1440x810'
#分辨率
my_dpi=96
#图大小
plt.figure(figsize=(480/my_dpi,480/my_dpi), dpi=my_dpi)
plt.rcParams['font.sans-serif']=['SimHei']   # 用黑体显示中文
plt.rcParams['axes.unicode_minus']=False     # 正常显示负号

noData = '暂无数据!'
yesStr = '已判为面向用例'
noStr = '已判为正常作答'

class users:
    manualDict: dict

    def __init__(self, path):
        self.root = Tk()

        self.panedWindow = PanedWindow(self.root)
        self.panedWindow.pack(side='left')
        # 左边那个栏
        self.code_extracter = extracter('')
        self.basePATH = path
        self.root.title(path)
        self.root.geometry(size)

        with open(self.basePATH + '\\manual inspection.json', 'r+', encoding='utf8') as ff:
            if ff.read() == '':
                ff.write('{}')

        self.manualDict = eval(open(path + '\\manual inspection.json', encoding='utf8').read())

        self.yes_no_Button = ttk.Button(self.panedWindow, text=noData, command=self.changeCommentState, state='disabled')
        self.yes_no_Button.pack()

        self.extractButton = ttk.Button(self.panedWindow, text='数据提取', command=self.extractAction, state='disabled')
        self.extractButton.pack()
        self.chartButton = ttk.Button(self.panedWindow, text='show chart', command=self.showChart)
        self.chartButton.pack()
        self.userListBox = Listbox(self.panedWindow, width=18, height=30)
        self.userPathList = [item for item in list_files(path)
                        if item.endswith(".py") and not item.endswith('answer.py')]
        [self.userListBox.insert(self.userListBox.size(), str(item).split('\\')[3][5:-3])
         for item in self.userPathList]
        self.userListBox.bind('<Double-Button-1>', self.userCallOn)
        self.userListBox.pack()
        self.true_answer_button = ttk.Button(self.panedWindow, text='answer', command=self.answerAction)
        self.true_answer_button.pack()
        self.readmeButton = ttk.Button(self.panedWindow, text='readme', command=self.readmeAction)
        self.readmeButton.pack()
        self.test_case_button = ttk.Button(self.panedWindow, text='test-cases', command=self.testCaseAction)
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

    def refreshTextColor(self, aList, string):
        pass

    def readUserYN(self):
        a = self.userPathList[self.userListBox.curselection()[0]]
        result = self.manualDict.get(a)
        if result is None:
            return noData
        else:
            return result

    def changeCommentState(self):
        oldString = self.yes_no_Button['text']
        if oldString == noData or oldString == noStr:
            newString = yesStr
        else:
            newString = noStr

        self.yes_no_Button['text'] = newString
        self.writeUserYN(newString)

    def writeUserYN(self, newString):
        a = self.userPathList[self.userListBox.curselection()[0]]
        self.manualDict[a] = newString

        with open(self.basePATH + '\\manual inspection.json', 'w', encoding='utf8') as ff:
            ff.write(str(self.manualDict))

    def gotoUserState(self):
        self.extractButton.configure(state='normal')
        self.yes_no_Button.configure(state='normal')

    def exitUserState(self):
        self.extractButton.configure(state='disabled')
        self.yes_no_Button.configure(state='disabled')

    def userCallOn(self, event):
        my_path = self.userPathList[self.userListBox.curselection()[0]]
        code = open(my_path, encoding='utf8').read()
        self.code_extracter = extracter(code)
        self.refreshTextByString(code)
        self.gotoUserState()
        self.yes_no_Button['text'] = self.readUserYN()
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

    def showChart(self):
        # height
        height = [3, 12, 5, 18, 45,
                  3, 12, 5, 18, 45,
                  3, 12, 5, 18, 45,
                  3, 12, 5, 18, 45,
                  3, 12, 5, 18, 45,
                  3, 12, 5, 18, 45,
                  3, 12, 5, 18, 45,
                  3, 12, 5, 18, 45,
                  3, 12, 5, 18, 45,
                  3, 12, 5, 18, 45,
                  3, 12, 5, 18, 45,
                  3, 12, 5, 18, 45,
                  3, 12, 5, 18, 45
                  ]
        # name of each column
        bars = ['A', 'B', 'C', 'D', 'E',
                'A', 'B', 'C', 'D', 'E',
                'A', 'B', 'C', 'D', 'E',
                'A', 'B', 'C', 'D', 'E',
                'A', 'B', 'C', 'D', 'E',
                'A', 'B', 'C', 'D', 'E',
                'A', 'B', 'C', 'D', 'E',
                'A', 'B', 'C', 'D', 'E',
                'A', 'B', 'C', 'D', 'E',
                'A', 'B', 'C', 'D', 'E',
                'A', 'B', 'C', 'D', 'E',
                'A', 'B', 'C', 'D', 'E',
                'A', 'B', 'C', 'D', 'E'
                ]
        bars = [i*5 for i in bars]
        y_pos = np.arange(len(bars))
        # draw column
        plt.bar(y_pos, height)
        # x
        plt.xticks(y_pos, bars, rotation=270)
        plt.show()
