from fabric.api import local

CMD_MANAGE = "python manage.py "

def auto_schema():
    schema('rockit')
    schema('rockit.plugins.mailout')
    schema('rockit.plugins.razberry')

def build():
    migrate('rockit')
    migrate('rockit.plugins.mailout')
    migrate('rockit.plugins.razberry')
    
    load_data('rockit/foundation/core/fixtures/settings.json')
    load_data('rockit/plugins/mailout/fixtures/servers.json')

    test()

def celery():
    local("python manage.py celeryd worker --loglevel=DEBUG  -E -B -c 1")

def load_data(path):
    local(CMD_MANAGE + 'loaddata %s' % path)

def migrate(app):
    local(CMD_MANAGE + 'migrate %s' % app)

def runserver(localonly=True):
    if localonly:
        local(CMD_MANAGE + 'runserver')
    else:
        local(CMD_MANAGE + 'runserver 0.0.0.0')

def schema(app):
    local(CMD_MANAGE + 'schemamigration %s --auto' % app)

def setup(environment):
    local('pip install -r requirements/%s' % environment)

def test():
    local(CMD_MANAGE + 'test')