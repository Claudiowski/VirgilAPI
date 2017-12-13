class Config:
    pass

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    
    DEBUG = True

    DB_URI = "postgresql://"
    DB_USER = "virgil"
    DB_PASSWORD = "virgil"
    DB_HOST = "localhost"
    DB_NAME = "virgildb"


config = {
    'default': Config,
    'production': ProductionConfig,
    'development': DevelopmentConfig
}