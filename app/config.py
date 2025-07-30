import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class Config:
    # 新增：添加CSRF所需的密钥配置
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-for-development-only'
    ARK_API_KEY = os.getenv('ARK_API_KEY', '')
    ACCESS_KEY = os.getenv('ACCESS_KEY', '')

    # 新增：全局禁用CSRF保护（纯后端API无需CSRF）
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_recycle': 3600,
        'pool_pre_ping': True
    }

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_recycle': 3600,
        'pool_pre_ping': True
    }

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'mysql+pymysql://root:password@localhost/dev_db'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'mysql+pymysql://root:password@localhost/test_db'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://root:password@localhost/prod_db'

# 配置映射
config_by_name = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig
}
