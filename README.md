# Python-exam---program

API Documentation - https://jsonplaceholder.typicode.com/posts

Used library:                       - requests
                                    - logging
                                    - re
                                    - json
                                    - marshmallow
                                    - Validation

test.py                             - collects all test calls   
Data_extract.py                     - the file with test datas
Config.json                         - the file with api endpoint, log file 
Request_post.py                     - posts the data to REST endpoint, validates and checking the returned data
Data.txt                            - the file with input text datas
requirements.txt                    - includes all required libraries for this project

Classes:
Api_class()                         - for api post requestsing
ApiSchema()                         - for validating the api response data with schema

Functions:
get_data_file                       - for getting test datas from text file  
