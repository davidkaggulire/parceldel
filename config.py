"""config.py"""

class Config:
    """parent config class"""
    DEBUG = False

class TestingConfig(Config):
    """Testing config class"""
    DEBUG = True

class DevelopmentConfig(Config):
    """development config class"""
    DEBUG = False

app_config = {
    "testing_config": TestingConfig,
    "development_config": DevelopmentConfig
}
