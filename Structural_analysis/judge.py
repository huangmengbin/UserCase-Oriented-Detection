import math


def writer(s):
    w = open('result', 'a+')
    w.write(s)
    w.write("\n")
    w.close()

def judge(matrix,user_id):
    _is_=0

    writer(user_id+"     "+str(_is_))

def reader():
    # str.endswith(".zip\n")
    # str.endswith(".py\n")
    # str.startswith("\n\n")
    f = open('goodNight', 'r', encoding='UTF-8')
    case_num = 0
    if_num = 0
    str = ''
    matrix = []
    try:
        while True:
            str = f.readline()
            if (str.endswith(".zip\n")):
                case_id=str[11:str.find("_")]
                writer("case_id:"+case_id)
                f.readline()
                case_num = int(f.readline())
            if str.endswith(".py\n"):
                user_id=str[str.find('r')+2:str.find("r")+7]
                f.readline()
                if_num = int(f.readline())
                f.readline()
                f.readline()
                if(math.fabs(case_num-if_num) >3) or if_num==0:
                    continue
                while True:
                    s = f.readline()
                    if s.startswith("="):
                        print(matrix)
                        matrix = []
                        break
                    matrix.append(s[s.find('[') + 1:s.find(']')])
                judge(matrix,user_id)
            #break
        f.close()
    except Exception:
        print('打不开')

if __name__ == '__main__':
    reader()