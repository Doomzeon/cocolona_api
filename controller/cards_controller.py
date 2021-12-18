import logging
from utils.aws_s3 import AWSS3Bucket
import json
from flask import Response


class CardController:
    def __init__(self, type: str):
        self.type = type

    def get_card_by_type(self):
        try:
            logging.info(f"Trying to get url for image with type : {self.type}")
            if self.type == "WML":
                awss3_bucket = AWSS3Bucket(bucket_name=self.type)
                return Response(
                    self.__build_payload_response(
                        message="OK", payload=awss3_bucket.get_image_url()
                    ),
                    status=200,
                    mimetype="application/json",
                )
            elif self.type == "WMM":
                awss3_bucket = AWSS3Bucket(bucket_name=self.type)
                return Response(
                    self.__build_payload_response(
                        message="OK", payload=awss3_bucket.get_image_url()
                    ),
                    status=200,
                    mimetype="application/json",
                )
            elif self.type == "WMC":
                awss3_bucket = AWSS3Bucket(bucket_name=self.type)
                return Response(
                    self.__build_payload_response(
                        message="OK", payload=awss3_bucket.get_image_url()
                    ),
                    status=200,
                    mimetype="application/json",
                )
            elif self.type == "WW":
                awss3_bucket = AWSS3Bucket(bucket_name=self.type)
                return Response(
                    self.__build_payload_response(
                        message="OK", payload=awss3_bucket.get_image_url()
                    ),
                    status=200,
                    mimetype="application/json",
                )
            else:
                return Response(
                    self.__build_payload_response(
                        message="Not found", status=404, mimetype="application/json"
                    )
                )
        except Exception as e:
            logging.error(f"An error occured {e}")
            return Response(
                self.__build_payload_response(message="Internal server errore"),
                status=500,
                mimetype="application/json",
            )

    def __build_payload_response(self, message: str, payload=None) -> dict:
        return json.dumps({"message": message, "payload": payload})
