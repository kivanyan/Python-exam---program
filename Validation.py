import logging
from marshmallow import Schema, fields, ValidationError


class ApiSchema(Schema):
    userId = fields.Number(required=True)
    title = fields.String(required=True)
    body = fields.String(required=True)
    id = fields.Number(required=True)

    def check_validation(self, json_data, log_file):
        self.json_data = json_data
        self.log_file = log_file
        logging.basicConfig(filename=self.log_file, encoding='utf-8', format='%(asctime)s: - %(levelname)s:%(message)s', level=logging.DEBUG)

        try:
            result = ApiSchema().load(self.json_data)
        except ValidationError as x:
            logging.error(x.messages)
        else:
            logging.info("Validation ok")
