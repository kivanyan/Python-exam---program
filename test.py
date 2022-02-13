import json
import logging
import Request_post
from Data_extract import get_data_file


with open(r'C:\Users\user\Desktop\Automation_testing_group\Python_Exam\Karine_Ivanyan_exam_last\Karine_Ivanyan_exam\Config.json', "r") as file:
    my_dict = json.load(file)


url_post = my_dict["url_post"]
dict_req = get_data_file()
log_file = my_dict["log_file"]


obj_call = Request_post.Api_class(url_post, dict_req, log_file)
dict_resp = obj_call.api_request()
check = obj_call.checking_new_data(dict_resp, dict_req, log_file)
