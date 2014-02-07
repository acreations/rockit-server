from fabric.api import local
from fabric.api import warn_only

CMD_MANAGE = "python manage.py "

def auto_schema():
    with warn_only():
        schema('rockit.foundation.core')
        schema('rockit.plugins.mailout')

def build():
    migrate('rockit.foundation.core')
    migrate('rockit.plugins.mailout')
    
    load_data('rockit/foundation/core/fixtures/settings.json')
    load_data('rockit/plugins/mailout/fixtures/servers.json')

    test()

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