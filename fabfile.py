from fabric.api import local
from fabric.api import warn_only

def auto_migrate():
	with warn_only():
		local('python manage.py schemamigration rockit.foundation.core --auto')	

def setup(environment):
	local('pip install -r requirements/' + environment)