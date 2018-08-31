import os

class Config:

    HIGHLIGHTS_API_BASE_URL ='https://newsapi.org/v2/top-headlines?country={}&category={}&apiKey={}'
    HIGHLIGHTS_API_KEY = os.environ.get('HIGHLIGHTS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}