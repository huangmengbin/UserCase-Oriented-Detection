import os
import shutil


def list_files(_path):
    if os.path.isdir(_path):
        return [_path + "\\" + i for i in os.listdir(_path)]
    else:
        return []


def isPython(_path):
    if not os.path.exists(_path):
        return False
    f = open(_path, encoding='utf8')
    res = f.read()
    return res.find('Python') >= 0 and res.find('C++') == -1


PATH = "D:\\"+"czyFile"

problems = list_files(PATH)
for problem in problems:
    print("=======================================================\n\n"+problem)
    users = list_files(problem)
    basePATH = users[0] + "\\"
    shutil.copy(src=basePATH+"readme.md", dst=problem+"\\readme.md")
    shutil.copy(basePATH+".mooctest\\testCases.json", problem+"\\testCases.json")
    shutil.copy(basePATH + ".mooctest\\answer.py", problem + "\\answer.py")
    open(problem+"\\res.json", "w").close()
    for user in users:
        answer = user + "\\main.py"
        if os.path.exists(answer) and isPython(user + "\\properties"):
            userName = user.split("\\")[-1].replace("_unzip", ".py")
            print(userName)
            shutil.copy(src=answer, dst=problem + "\\" + userName)
            shutil.rmtree(user)  # 最后执行这个
