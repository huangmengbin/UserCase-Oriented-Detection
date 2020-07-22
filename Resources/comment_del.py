import re
import ast



from Resources.cut_paste_rename import list_files as list_files
import py_compile

def file_analysis(old_file_lines, six_quotes, hashtap):

    """标记需要删除的注释的行号，并存入列表"""
    i = 0
    for line in old_file_lines:
        # 符号 # 独占一行
        ret_1 = re.match(r"^[^\w]*#+", line)
        if ret_1:
            hashtap.append(i)
        # 符号 """ 独占一行
        ret_2 = re.match(r"[ ]*\"\"\"", line)
        if ret_2:
            # 如果存在类型，函数说明的 """xxxxx""" 之类的，不予删除
            ret_2_1 = re.match(r"[^\"]*\"\"\"[^\"]*\"\"\"", line)
            if ret_2_1:
                pass
            else:
                six_quotes.append(i)
        i += 1
    # 将两个"""行号之间所有的行添加到 # 号列表中
    while six_quotes != []:
        # 从列表中移出最后两个元素
        a = six_quotes.pop()
        b = six_quotes.pop()
        temp = b
        while temp <= a:
            hashtap.append(temp)
            temp += 1
    # 返回 # 号列表， 记返回需要删除的所有注释的 行号 集合
    return hashtap


def main():
    """ 主函数"""
    # 1，获取路径，并读取此文件

    # 1.1 获取文件名及其路径
    print("\r\n" * 3)
    file_name = input("请输入需要删除注释的目标文件（形如：file.py）：")
    # 1.2 读取文件
    try:
        f = open(file_name, "rb")
        old_file = f.read()
        f.close()
    except:
        print("无法打开文件：" + file_name)
    else:
        # 2，处理文件
        # 2.1 读取文件成功，文件解码并按行切割成列表
        old_file = old_file.decode("utf-8")
        old_file_lines = old_file.splitlines()
        # 2.2 处理文件并得到需要删除的注释的行号集合
        six_quotes, hashtap = list(), list()
        hashtap = file_analysis(old_file_lines, six_quotes, hashtap)
        # 此时返回值 hashtap列表中，不仅仅包含#，还有"""的行号
        try:
            # 3，获取 注释和无注释 内容到列表中
            # 3.2 去重并排序，得到所有注释行号的列表
            comment_list = sorted(set(hashtap))
            # 3.3 创建存储(备份)注释文件内容的列表
            comment_file = list()
            for i in comment_list:
                comment = old_file_lines[i]
                comment_file.append(comment)
            # 创建与源文件总行号相同的列表 0,1,2,3...
            new_file_list = list(i for i in range(len(old_file_lines)))
            # 删除注释的行号，留下无注释的行号 的列表集合
            for i in comment_list:
                new_file_list.remove(i)
            # 3.4 创建存储（无注释）新文件内容的列表
            new_file_lines = list()
            for i in new_file_list:
                temp = old_file_lines[i]
                new_file_lines.append(temp)

        except:
            print("待处理代码中没有注释")
        else:
            # 4，在文件路径新建两个文件，并写入数据到文件
            ret = re.match(r"([^ ]+).py", file_name)
            if ret:
                file_name_pre = ret.group(1)
                # 5，分别新建 “干净版”文件，和“注释集合”文件
                with open(file_name_pre + "(无注释版).py", "wb") as f:
                    for i in new_file_lines:
                        f.write(i.encode("utf-8"))
                        f.write("\r\n".encode("utf-8"))
                with open(file_name_pre + "(注释存档).txt", "wb") as f:
                    for i in comment_file:
                        f.write(i.encode("utf-8"))
                        f.write("\r\n".encode("utf-8"))
                print("\r\n" * 3)
                print("--------创建成功！！！--------")
                print("\r\n" * 3)
            else:
                print("正则字符串，无法识别文件的路径")


if __name__ == "__main__":
   main()
