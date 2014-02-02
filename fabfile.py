from fabric.api import local
from fabric.api import warn_only

def auto_schema():
    with warn_only():
        schema('rockit.foundation.core')
        schema('rockit.plugins.mailout')

def build():
    migrate('rockit.foundation.core')
    test()	

def migrate(app):
    local('python manage.py migrate %s' % app)

def schema(app):
    local('python manage.py schemamigration %s --auto' % app)

def setup(environment):
    local('pip install -r requirements/%s' % environment)

def test():
    local('python manage.py test')