class Config:
    
    DB_URI = "postgresql://"
    DB_USER = "virgil"
    DB_PASSWORD = "virgil"
    DB_HOST = "localhost"
    DB_NAME = "virgildb"


class ProductionConfig(Config):

    DEBUG = True


class DevelopmentConfig(Config):
    
    pass


config = {
    'default': Config,
    'production': ProductionConfig,
    'development': DevelopmentConfig
}