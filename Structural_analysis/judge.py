import math
from func_timeout import func_set_timeout
import func_timeout.exceptions

def writer(s):
    w = open('result', 'a+',encoding="UTF-8")
    w.write(s)
    w.write("\n")
    w.close()


def judge(beforeDeleteIf, matrix, user_id, yyf):
    if not yyf:
        _is_ = 0
        _valid = (beforeDeleteIf).count(1)/len(beforeDeleteIf)
    else:
        # todo
        '''
        有一个，没删前的beforeDeleteIf，看看有几个1？0个 1个 直接和上面一样算了，不管了。
        beforeDeleteIf若有0，把大矩阵对应的 列 删了。本来都不能过测试，之后肯定也不能过
        然后，这个矩阵，把全1的 行 都删了，说明这个if可能根本就没执行到
        现在就剩下一个矩阵了
        '''
        _is_ = 1
        _valid = (beforeDeleteIf).count(1)/len(beforeDeleteIf)  * 0.9
        count=0
        for i in range(0,len(beforeDeleteIf)):
            if beforeDeleteIf[i] == 0:
                for j in range(0,len(matrix)):
                    matrix[j].pop(i-count)
                count+=1

        for i in matrix:
            if i.count(1)==len(i):
                matrix.remove(i)
                count+=1


        num_zero=0  #0的行数
        for i in matrix:
            if i.count(0)==len(i):
                num_zero+=1
        if(num_zero>1):
            _is_=0
            _valid=1.0


        two_zero=0  #两个0的行数
        for i in matrix:
            if i.count(0)>1:
                two_zero+=1
        if(two_zero>0):
            _is_ = 0
            _valid = 0.9

        zero_num=0  #0的个数
        for i in matrix:
            zero_num+=i.count(0)
        if(math.fabs(zero_num-(len(beforeDeleteIf)-count))>1):
            _is_=0

        if(matrix==[] or (matrix[0])==[]):
            _is_=0
            _valid=0.0


    writer(user_id + "     " + str(_is_) + "    " + str(_valid))

@func_set_timeout(60)
def reader():
    # str.endswith(".zip\n")
    # str.endswith(".py\n")
    # str.startswith("\n\n")
    f = open('goodNight', 'r', encoding='UTF-8')
    case_num = 0
    if_num = 0
    str = ''
    matrix = []
    # try:
    while True:
        str = f.readline()
        if (str.endswith(".zip\n")):
            case_id = str[11:str.find("_")]
            writer("case_id:" + case_id)
            f.readline()
            case_num = int(f.readline())
        if str.endswith(".py\n"):
            user_id = str.split('\\')[3].split('_')[1]#str[str.find('r') + 2:str.find("r") + 7]
            f.readline()
            if_num = int(f.readline())
            s = f.readline()
            beforeDelif = list(map(int, (s[10:s.find(']')]).split(',')))
            print(beforeDelif)
            f.readline()
            yyf = True
            if (math.fabs(case_num - if_num) > 3) or if_num == 0:
                yyf = False

            while True:
                s = f.readline()
                if s.startswith("="):
                    print(matrix)
                    judge(beforeDelif, matrix, user_id, yyf)
                    matrix = []
                    break
                matrix.append(list(map(int, s[1:s.find("]")].split(","))))



            # break
        # f.close()
    # except Exception:
    #     print('打不开')

if __name__ == '__main__':
    reader()