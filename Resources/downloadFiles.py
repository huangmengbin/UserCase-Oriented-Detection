import json
import os
import urllib.parse, urllib.request
import zipfile

#  本代码要在F盘创建code_data1才能运行
def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            L.append(os.path.join(root, file))
    return L


def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)
    else:
        print('This is not zip')


def remove_file(path):
    if os.path.exists(path):  # 如果文件存在
        os.remove(path)
        print("解压完成,已删除" + path)


f = open('hmbSB.json', encoding='utf8')
res = f.read()
data = json.loads(res)
for case in data:
    print(case['case_id'])
    filename=urllib.parse.unquote(os.path.basename(case["case_zip"]))
    if not os.path.exists("F:\\"+"code_data1\\" + str(case["case_id"])+"_" +str(case["case_type"])+"_"+filename):
        os.mkdir("F:\\"+"code_data1\\" + str(case["case_id"])+"_" +str(case["case_type"])+"_"+filename)
    for user in case['all_users']:
        print(user)
        filename_= user
        if not os.path.exists("F:\\"+"code_data1\\" + str(case["case_id"]) +"_"+str(case["case_type"])+"_"+filename+ "\\" +"user_"+ filename_ +"_score_"+str(case['all_users'][user]["score"]) + "_unzip\\"):
            try:
                urllib.request.urlretrieve(case['all_users'][user]["lastUpdate"],
                                           "F:\\"+"code_data1\\" + str(case["case_id"])+"_"+str(case["case_type"]) +"_"+filename+ "\\"+"user_"+ filename_ +"_score_"+str(case['all_users'][user]["score"]))
            except Exception as e:
                print(e)

            try:
                os.mkdir("F:\\"+"code_data1\\" + str(case["case_id"])+"_"+str(case["case_type"])+"_"+filename + "\\" +"user_"+ filename_ +"_score_"+str(case['all_users'][user]["score"])+ "_unzip\\")

                unzip_file("F:\\"+"code_data1\\" + str(case["case_id"])+"_"+str(case["case_type"])+"_"+filename + "\\" +"user_"+ filename_ +"_score_"+str(case['all_users'][user]["score"]),
                           "F:\\"+"code_data1\\" + str(case["case_id"])+"_"+str(case["case_type"]) +"_"+filename+ "\\" +"user_"+ filename_ +"_score_"+str(case['all_users'][user]["score"]) + "_unzip\\")  # 外层解压
                remove_file("F:\\"+"code_data1\\" + str(case["case_id"])+"_"+str(case["case_type"])+"_"+filename + "\\" +"user_"+ filename_ +"_score_"+str(case['all_users'][user]["score"]))  # 解压后删除压缩包

                zip_name = file_name("F:\\"+"code_data1\\" + str(case["case_id"])+"_"+str(case["case_type"])+"_"+filename + "\\" +"user_"+ filename_ +"_score_"+str(case['all_users'][user]["score"])+ "_unzip\\")[
                    0]
                unzip_file(zip_name,
                           "F:\\"+"code_data1\\" + str(case["case_id"]) +"_"+str(case["case_type"])+"_"+filename+ "\\" +"user_"+ filename_ +"_score_"+str(case['all_users'][user]["score"]) + "_unzip\\")  # 内层解压
                remove_file(zip_name)  # 解压后删除压缩包
            except Exception as e:
                print(e)
    print("========================================分割线======================================================")