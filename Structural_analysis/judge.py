import math


def writer(s):
    w = open('result', 'a+')
    w.write(s)
    w.write("\n")
    w.close()


def judge(beforeDeleteIf, matrix, user_id, yyf):
    if not yyf:
        _is_ = 0
        _valid = 0
    else:
        # todo
        '''
        有一个，没删前的beforeDeleteIf，看看有几个1？0个 1个 直接和上面一样算了，不管了。
        beforeDeleteIf若有0，把大矩阵对应的 列 删了。本来都不能过测试，之后肯定也不能过
        然后，这个矩阵，把全1的 行 都删了，说明这个if可能根本就没执行到
        现在就剩下一个矩阵了
        
        '''
        _is_ = 1
        _valid = 1

    writer(user_id + "     " + str(_is_) + " " + str(_valid))


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
                case_id = str[11:str.find("_")]
                writer("case_id:" + case_id)
                f.readline()
                case_num = int(f.readline())
            if str.endswith(".py\n"):
                user_id = str[str.find('r') + 2:str.find("r") + 7]
                f.readline()
                if_num = int(f.readline())
                beforeDelif = eval(f.readline()[9:])
                f.readline()

                yyf = True

                if (math.fabs(case_num - if_num) > 3) or if_num == 0:
                    # 这里同样要跑到judge那里去，也要写啊
                    yyf = False
                while yyf:
                    s = f.readline()
                    if s.startswith("="):
                        print(matrix)
                        matrix = []
                        break

                    matrix.append(eval(s))
                print(beforeDelif)
                judge(beforeDelif, matrix, user_id, yyf)
            # break
        # f.close()
    except Exception:
        print('打不开')


if __name__ == '__main__':
    reader()
