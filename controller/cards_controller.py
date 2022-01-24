import logging
from utils.aws_s3 import AWSS3Bucket
import json
from flask import Response


class CardController:
    def __init__(self, type: str):
        self.type = type
        self.__text = None
        self.__url = None
        self.awss3_bucket = AWSS3Bucket()


    def get_card_by_type(self):
        try:
            logging.info(f"Trying to get url for image with type : {self.type}")
            if self.type == "WML":
                self.__text = self.awss3_bucket.get_random_text_for_card(file= 'wml')
            elif self.type == "WMM":
                self.__text = self.awss3_bucket.get_random_text_for_card(file= 'wmm')
            elif self.type == "WMC":
                self.__text = self.awss3_bucket.get_random_text_for_card(file= 'wmc')
            elif self.type == "WW":
                self.__text = self.awss3_bucket.get_random_text_for_card(file= 'lesbian')
            
            return Response(
                self.__build_payload_response(
                    message="OK", payload={"text":self.__text}
                ),
                status=200,
                mimetype="application/json",
            )
        except Exception as e:
            logging.error(f"An error occured inside get_card_by_type {e}")
            return Response(
                self.__build_payload_response(message="Internal server errore"),
                status=500,
                mimetype="application/json",
            )

    def __build_payload_response(self, message: str, payload=None) -> dict:
        return json.dumps({"message": message, "payload": payload})
