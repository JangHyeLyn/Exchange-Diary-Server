SECRET = {
    'SECRET_KEY': '4j2mz03tg+dpw_m48=e)i5)1^de%a=7fzc++juwounvs@o^m@n',

    ## Oauth providers
    'SOCIALACCOUNT_PROVIDERS': {
        'kakao': {
            'APP': {
                'client_id': 'de4e96410888c9be02304c66371ea680',
                'secret': 520682,
                'key': ''
            }
        }
    },

    'DATABASE_DEV': {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'exchange',
            'USER': 'root',
            'PASSWORD': 'schwisestudy',
            'HOST': 'wisestudy.cinqw7ouyrxc.ap-northeast-2.rds.amazonaws.com',
            'PORT': 3306,
            'OPTIONS': {
                'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
            }
        }
    },
    'DATABASE_TEST': {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'exchange_test',
            'USER': 'root',
            'PASSWORD': 'schwisestudy',
            'HOST': 'wisestudy.cinqw7ouyrxc.ap-northeast-2.rds.amazonaws.com',
            'PORT': 3306,
            'OPTIONS': {
                'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
            }
        }
    },
    'AWS_ACCESS_KEY_ID': 'AKIAWVQALOFDSSIOX7S2',
    'AWS_SECRET_ACCESS_KEY': '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'
}