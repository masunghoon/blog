CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

##### DATABASE ####################################
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_RECORD_QUERIES = True
# SQLALCHEMY_DATABASE_URI = 'mysql://ghas:rudwkrh@masunghoon.iptime.org/masunghoon'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app_db1.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


# pagination
POSTS_PER_PAGE = 3