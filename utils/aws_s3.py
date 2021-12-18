import boto3
import random
import logging


class AWSS3Bucket:
    def __init__(self, folder: str) -> None:
        self.folder = folder
        self.__key == "AKIAWEDK34F77LWA2JW6" # store to env file
        self.__secret_access_key = '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'
        self.bucket_name = 'cocolonacards' # store to env file
        self.s3 = boto3.client("s3", aws_access_key_id= self.__key, aws_secret_access_key= self.__secret_access_key)
        self.bucket = self.s3.Bucket()

    def get_image_url(self):
        try:
            logging.info(f'Trying to generate presigned url for s3 bucket')
            url = self.s3.generate_presigned_url(
                "get_object",
                Params={
                    "Bucket": self.bucket_name,
                    "Key": f"{self.folder}/{self.__get_random_image()}.jpeg",
                },
                ExpiresIn=3600,
            )
            logging.info(f'Gnerated url: {url}')
            return url
        except Exception as e:
            logging.error(f"An error occured {e}")

    def __get_random_image(self):
        try:
            logging.info(f'Generating random number of image')
            number_images = self.__count_image_inside_bucket()
            image_name = random.randint(0, number_images)
            logging.info(f'Generated number {image_name}')
            return image_name
        except Exception as e:
            logging.error(f"An error occured {e}")

    def __count_image_inside_bucket(self):
        try:
            logging.info(
                f"Trying to calculate images inside the bucket {self.bucket_name}"
            )
            totalCount = 0
            for key in self.bucket.objects.filter(Prefix=f"{self.folder}/"):
                totalCount += 1
            logging.info(
                f"Calculated {totalCount} inside the bucket {self.bucket_name}"
            )
            return totalCount
        except Exception as e:
            logging.error(f"An error occured {e}")
