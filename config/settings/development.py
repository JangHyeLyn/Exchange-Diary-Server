from .base import *

ALLOWED_HOSTS = ['*']

DATABASES = SECRET['DATABASE_DEV']

# aws s3
AWS_ACCESS_KEY_ID = SECRET['AWS_ACCESS_KEY_ID'] # .csv 파일에 있는 내용을 입력 Access key ID
AWS_SECRET_ACCESS_KEY = SECRET['AWS_SECRET_ACCESS_KEY'] # .csv 파일에 있는 내용을 입력 Secret access key
AWS_REGION = 'ap-northeast-2'

###S3 Storages
AWS_STORAGE_BUCKET_NAME = 'exchange-diary-bucket' # 설정한 버킷 이름
AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (AWS_STORAGE_BUCKET_NAME,AWS_REGION)
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

INSTALLED_APPS +=[
    'debug_toolbar',
    'django_seed',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

INTERNAL_IPS = ['127.0.0.1']