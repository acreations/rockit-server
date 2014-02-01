from fabric.api import local
from fabric.api import warn_only

def auto_migrate():
	with warn_only():
		local('python manage.py schemamigration rockit.foundation.core --auto')	

def build():
	migrate('rockit.foundation.core')
	test()

def migrate(app):
	local('python manage.py migrate ' + app)

def setup(environment):
	local('pip install -r requirements/' + environment)

def test():
	local('python manage.py test')