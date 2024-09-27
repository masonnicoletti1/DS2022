#!/bin/bash

IMAGEURL="https://t4.ftcdn.net/jpg/06/36/02/73/240_F_636027337_QscKpKYKr4bdNk7U5hYZPHcYeC6f6MRL.jpg"
IMAGEFILE="beach.jpg"
BUCKET="ds2022-cxx6sw"

#Get image from web
curl $IMAGEURL > $IMAGEFILE

#Upload image file to s3 bucket
aws s3 cp $IMAGEFILE s3://$BUCKET/

#Create expiring url of image
aws s3 presign --expires-in 604800 s3://$BUCKET/$IMAGEFILE

