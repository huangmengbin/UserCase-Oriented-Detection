from tkinter import *
from tkinter import  ttk
from Resources.cut_paste_rename import list_files
from String_match import Partial_ratio
from String_match.extract_data import Extracter
from typing import Dict
import numpy as np
import matplotlib.pyplot as plt
from String_match.partial_ratio import *
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


def getColor(string):
    if string is None:
        return 'b'
    elif string == noStr:
        return 'g'
    elif string == yesStr:
        return 'r'
    else:
        return 'b'


class users:
    partial_ratioDict: Dict[str, Partial_ratio]
    partial_ratio: Partial_ratio
    jsonParser: JsonParser
    manualDict: dict

    def __init__(self, path, jsonParser):
        self.root = Tk()
        self.jsonParser = jsonParser
        self.panedWindow = PanedWindow(self.root)
        self.panedWindow.pack(side='left')
        # 左边那个栏

        self.partial_ratio = Partial_ratio('', jsonParser)
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

        self.partial_ratioDict = self.__initRatioDict()

    def __initRatioDict(self):
        result = dict()
        for path in self.userPathList:
            code = open(path, encoding='utf8').read()
            partial_ratio = Partial_ratio(code=code, jsonParser=self.jsonParser)
            result[path] = partial_ratio
        return result

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

    def refreshTextColor(self, color):
        aList = self.partial_ratio
        text_content = (self.textView.get("0.0", "end"))

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
        self.partial_ratio = self.partial_ratioDict.get(my_path)
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
        self.refreshTextByString(self.partial_ratio.extracter.afterExtractCode)
        self.exitUserState()
        pass

    def showChart(self):
        # height
        keys = [i for i in self.partial_ratioDict.keys()]
        keys.sort(key=lambda i: self.partial_ratioDict.get(i).outData[0])

        height = [(self.partial_ratioDict.get(i).outData[0]) for i in keys]

        bars = [(i.split('\\')[-1]).split('_')[1] for i in keys]
        y_pos = np.arange(len(bars))

        colorList = [getColor(self.manualDict.get(i)) for i in keys]

        plt.bar(y_pos, height, color=colorList)
        # x
        plt.xticks(y_pos, bars, rotation=270)
        plt.show()
