#!/home/codespace/.python/current/bin/python3

import os
import boto3
import urllib.request

image_url = "https://t3.ftcdn.net/jpg/06/26/71/36/360_F_626713659_a9FhZtViYUooPSvqme2ZZIIvr7Qg5yBY.jpg"
#image_url2 = "https://c4.wallpaperflare.com/wallpaper/179/223/759/underwater-water-sun-rays-nature-wallpaper-preview.jpg"
image_name = "underwater.jpg"
bucket = 'ds2022-cxx6sw'

#Fetch image from online
image = urllib.request.urlretrieve(image_url, image_name)

#Create an s3 client
s3 = boto3.client('s3', region_name='us-east-1')

#Upload file to bucket
with open(image_name, 'wb') as file_data:
    resp = s3.put_object(
        Body = image_name, 
        Bucket = bucket,
        Key = image_name,
    )

#Presign file with expiration time
response = s3.generate_presigned_url(
    'get_object',
    Params = {'Bucket': bucket, 'Key': image_name},
    ExpiresIn = 604800
)

#Output presigned url
print(response)
