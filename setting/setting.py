LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        # プロジェクト用のフォーマットを追加
        'heibon': {
            'format': '\t'.join([
                "[%(levelname)s]",
                "%(asctime)s",
                "%(name)s:%(lineno)d",
                "%(message)s",
                "%(threadName)s",
            ])
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'heibon'
        },
    },
    "root": {
        "level": "DEBUG",
        "handlers": [
            "console"
        ]
    },
    'loggers': {
        'heibon.sample': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}

# from setting import setting
# from logging import config, getLogger

# config.dictConfig(setting.LOGGING)
# logger = getLogger(__name__)
