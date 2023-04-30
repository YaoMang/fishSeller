import os
import json

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

def read_json(project_path,json_file:str)     :
    for project in project_path:
        jsonfile=open(project+"/"+json_file)
        
    # json_dict:dict=json.loads(jsonfile.read())    
    # print(json_dict)

file_dir="./top_300_metrics"
dir_list=os.listdir(file_dir)
project_path=[]
for cur_file in dir_list:
    user=os.listdir(os.path.join(file_dir,cur_file))
    for repository in user:
        project_path.append(os.path.join(file_dir,cur_file)+'/'+repository)

read_json(project_path,"activity.json")