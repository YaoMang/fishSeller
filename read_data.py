import os
import json
import PAM
import matplotlib.pyplot as plt
import re

# def list_dir(file_dir):
#   '''
#     通过 listdir 得到的是仅当前路径下的文件名，不包括子目录中的文件，如果需要得到所有文件需要递归
#   '''
#   print('\n\n<><><><><><> listdir <><><><><><>')
#   print ("current dir : {0}".format(file_dir))
#   dir_list = os.listdir(file_dir)
#   for cur_file in dir_list:
#     # 获取文件的绝对路径
#     path = os.path.join(file_dir, cur_file)
#     if os.path.isfile(path): # 判断是否是文件还是目录需要用绝对路径
#       print ("{0} : is file!".format(cur_file))
#     if os.path.isdir(path):
#       print ("{0} : is dir!".format(cur_file))
#       list_dir(path) # 递归子目录

# string = "/top_300_metrics/CleverRaven/Cataclysm-DDA"
# regex = r"/([^/]+)$"
# match = re.search(regex, string)

# if match:
#     result = match.group(1)
#     print(result)  # 输出 "Cataclysm-DDA"
# else:
#     print("没有匹配到结果。")


def read_json(project_path, json_file_list: str):
    counter = 1
    seven_metricsDict_list = []
    for project in project_path:
        for json_file in json_file_list:
            try:
                jsonfile = open(project+"/"+json_file)
            except FileNotFoundError:
                print("无法打开文件 " + project+"/"+json_file + "。请检查文件名是否正确。")
                break
            json_dict: dict = json.loads(jsonfile.read())
            seven_metricsDict_list.append(json_dict)
        pam = PAM.PAM(seven_metricsDict_list[0],
                      seven_metricsDict_list[1],
                      seven_metricsDict_list[2],
                      seven_metricsDict_list[3],
                      seven_metricsDict_list[4],
                      seven_metricsDict_list[5],
                      seven_metricsDict_list[6])
        evolutionScore: dict = pam.getPAM(["2017-01", "2020-01"])
        txt = json.dumps(evolutionScore)
        regex = r"/([^/]+)$"
        match = re.search(regex, project)
        match = match.group(0)
        print(str(counter)+"   ./output"+match+".json")
        counter += 1
        f = open("./output/"+match+".json", "w+")
        f.write(txt)
        # x = list(evolutionScore.keys())
        # y = list(evolutionScore.values())
        # print(x)
        # print(y)
        # plt.plot(x, y)

    # json_dict:dict=json.loads(jsonfile.read())
    # print(json_dict)


if __name__ == "__main__":
    file_dir = "./top_300_metrics"
    dir_list = os.listdir(file_dir)
    project_path = []
    for cur_file in dir_list:
        user = os.listdir(os.path.join(file_dir, cur_file))
        for repository in user:
            project_path.append(os.path.join(file_dir, cur_file)
                                + '/'+repository)

    read_json(project_path, ["issue_comments.json", "issues_new.json", "change_requests.json",
              "change_requests_reviews.json", "change_requests_accepted.json", "attention.json", "technical_fork.json"])
