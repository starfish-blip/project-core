import os

class Config:
    ENV = os.getenv("ENV", "development")
    DEBUG = ENV == "development"
    VERSION = "1.0.0"
