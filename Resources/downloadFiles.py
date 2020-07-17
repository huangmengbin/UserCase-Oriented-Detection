import json
import os
import urllib.parse
import urllib.request
import zipfile

basicFilePlace = "D:\\" + "czyFile\\"


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


def download_each_case(case):
    print(case['case_id'])
    filename = urllib.parse.unquote(os.path.basename(case["case_zip"]))
    if not os.path.exists(basicFilePlace + str(case["case_id"]) + "_" + str(case["case_type"]) + "_" + filename):
        os.mkdir(basicFilePlace + str(case["case_id"]) + "_" + str(case["case_type"]) + "_" + filename)

    for user in case['all_users']:
        print(case['case_id'], user)
        filename_ = user
        if not os.path.exists(basicFilePlace + str(case["case_id"]) + "_" + str(
                case["case_type"]) + "_" + filename + "\\" + "user_" + filename_ + "_score_" + str(
            case['all_users'][user]["score"])  ):

            try:
                urllib.request.urlretrieve(case['all_users'][user]["lastUpdate"],
                                           basicFilePlace + str(case["case_id"]) + "_" + str(case[
                                                                                                 "case_type"]) + "_" + filename + "\\" + "user_" + filename_ + "_score_" + str(
                                               case['all_users'][user]["score"]))
                print('downloaded')
            except Exception as e:
                print(e)

            # try:
            #     os.mkdir(basicFilePlace + str(case["case_id"]) + "_" + str(
            #         case["case_type"]) + "_" + filename + "\\" + "user_" + filename_ + "_score_" + str(
            #         case['all_users'][user]["score"]) + "_unzip\\")
            #
            #     unzip_file(basicFilePlace + str(case["case_id"]) + "_" + str(
            #         case["case_type"]) + "_" + filename + "\\" + "user_" + filename_ + "_score_" + str(
            #         case['all_users'][user]["score"]),
            #                basicFilePlace + str(case["case_id"]) + "_" + str(
            #                    case["case_type"]) + "_" + filename + "\\" + "user_" + filename_ + "_score_" + str(
            #                    case['all_users'][user]["score"]) + "_unzip\\")  # 外层解压
            #     remove_file(basicFilePlace + str(case["case_id"]) + "_" + str(
            #         case["case_type"]) + "_" + filename + "\\" + "user_" + filename_ + "_score_" + str(
            #         case['all_users'][user]["score"]))  # 解压后删除压缩包
            #
            #     zip_name = file_name(basicFilePlace + str(case["case_id"]) + "_" + str(
            #         case["case_type"]) + "_" + filename + "\\" + "user_" + filename_ + "_score_" + str(
            #         case['all_users'][user]["score"]) + "_unzip\\")[
            #         0]
            #     unzip_file(zip_name,
            #                basicFilePlace + str(case["case_id"]) + "_" + str(
            #                    case["case_type"]) + "_" + filename + "\\" + "user_" + filename_ + "_score_" + str(
            #                    case['all_users'][user]["score"]) + "_unzip\\")  # 内层解压
            #     remove_file(zip_name)  # 解压后删除压缩包
            # except Exception as e:
            #     print(e)

    print("========================================分割线======================================================")


if __name__ == '__main__':
    f = open('hmbSB.json', encoding='utf8')
    res = f.read()
    data = json.loads(res)
    for case in data:
        download_each_case(case)
