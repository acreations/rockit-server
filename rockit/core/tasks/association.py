from celery import task
from celery.utils.log import get_task_logger

from rockit.core import models

import uuid

@task(name='rockit.register.association')
def register(**kwargs):
    logger = register.get_logger()

    logger.debug("Trying to register association", kwargs)

    errors = dict()

    validate(errors, kwargs, "name")
    validate(errors, kwargs, "namespace")
    validate(errors, kwargs, "entry")

    # If no validation error then register
    if not bool(errors):

        association, created = models.Association.objects.get_or_create(**kwargs)

        return {
            'success': True,
            'created': created
        }

    return {
        'success': False,
        'errors': errors
    }


@task(name='rockit.unregister.association')
def unregister(uuid):
    logger = get_task_logger()

def validate(errors, kwargs, key):
    if key not in kwargs or not kwargs[key]:
        errors[key] = "%s cannot be empty" % key