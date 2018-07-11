__author__ = 'xianda'
import os

SECRET_KEY = os.urandom(24)
SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:2001170135@localhost:3306/xianda?charset=utf8'
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False