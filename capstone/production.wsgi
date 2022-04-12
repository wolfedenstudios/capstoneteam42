# production.wsgi
import sys
import os

sys.path.insert(0,"/var/www/html/CapstoneTeam42/")

def application(environ, start_response):
    for key in ['DB_NAME', 'DB_USERNAME', 'DB_PASSWORD', 'DB_HOSTNAME', 'SECRET_KEY']:
        os.environ[key] = environ.get(key, '')
        os.environ['FLASK_CONFIG'] = 'production'
        os.environ['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:React0r2020@localhost/team42adtaa'

    from app import app as _application

    return _application(environ, start_response)

