from celery import task
from celery.utils.log import get_task_logger

from rockit.core import models

import uuid

@task(name='rockit.register.association')
def register(**kwargs):
    logger = register.get_logger()

    association, created = models.Association.objects.get_or_create(**kwargs)

    return created



@task(name='rockit.unregister.association')
def unregister(uuid):
    logger = get_task_logger()
