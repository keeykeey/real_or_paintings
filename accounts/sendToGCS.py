import os

objToSend = ''
cloudStorageBucketName = 'real_or_picture'

#send object to cloud storage's bucker
os.system('gsutil cp {} gs://{}'.format(objToSend,cloudStrogeBucketName))

