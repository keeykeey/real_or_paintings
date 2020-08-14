#!/bin/bash

bucketName='real_or_picture'
objToSend='./animals/10264461753.jpg'

echo $bucketName

gsutil cp $objToSend gs://$bucketName
