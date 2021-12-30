import boto3
import random
import logging
import json
import os

class AWSS3Bucket:
    def __init__(self) -> None:
        self.__key_s3 = os.getenv("KEY_S3") # store to env file
        self.__secret_access_key = os.getenv('SECRET_ACCESS_KEY_S3')
        self.__bucket_name = os.getenv('BUCKET_NAME_S3') # store to env file
        
        self.s3 = boto3.client("s3", aws_access_key_id= self.__key_s3, aws_secret_access_key= self.__secret_access_key) #
        self.s3_resourse = boto3.resource('s3', aws_access_key_id= self.__key_s3, aws_secret_access_key= self.__secret_access_key)
        
    def get_image_url_v2(self, type):
        try:
            url = self.s3.generate_presigned_url(
                "get_object",
                Params={
                    "Bucket": self.__bucket_name,
                    "Key": f"cards/{type}.jpeg",
                },
                ExpiresIn=30600,
            )
            return url
        except Exception as e:
            logging.error(f"An error occured while getting image url {e}")
            raise(e)

    def get_random_text_for_card(self, file):
        try:
            logging.info(f'Generating random card text')
            content_object = self.s3_resourse.Object(self.__bucket_name, f'{file}.json')
            file_content = content_object.get()['Body'].read().decode('utf-8')
            file_json_text = json.loads(file_content)
            number_text_position = random.randint(0, len(file_json_text['texts']))
            logging.info(f'Generated number {number_text_position}')
            return file_json_text['texts'][number_text_position]
        except Exception as e:
            logging.error(f"An error occured while getting randome card text {e}")
            raise(e)

    