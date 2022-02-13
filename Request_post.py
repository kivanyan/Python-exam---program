import json
import logging
import requests
import Validation
from Data_extract import get_data_file

logging.basicConfig(filename='out.log', format='%(asctime)s: - %(levelname)s:%(message)s', level=logging.DEBUG)


class Api_class():
    def __init__(self, url_post, dict_req, log_file):
        self.url_post = url_post
        self.dict_req = dict_req
        self.log_file = log_file

    def api_request(self):

        try:
            response = requests.post(self.url_post, json=self.dict_req)
            status_code = response.status_code
            dict_resp = json.loads(response.text)

            assert int(status_code) in range(200, 209)
            logging.info("Success post!")

        except Exception as e:
            logging.exception(e)

        finally:
            json_response = json.loads(response.text)  #Nel, this line and line 21 is the same
            dict_resp = json_response #Nel, you compare the same response with it
        return dict_resp

    def checking_new_data(self, dict_resp, dict_req, log_file):
        self.dict_resp = dict_resp
        self.dict_req = dict_req
        obj_valid = Validation.ApiSchema()
        obj_valid.check_validation(dict_resp, log_file)

        check = dict_req != dict_resp
        dict_resp.pop("id")
        #check = dict_req == dict_resp #Nel, need to check this line to be sure that after pop you get the same request
        logging.info(check)
