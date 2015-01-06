from celery import task
from celery.utils.log import get_task_logger

from django.core import management

from rockit.core import models
from rockit.core import executors

import datetime
import celery
import uuid

logger = get_task_logger(__name__)

@task(name='rockit.register.node')
def register(namespace, node_id):
    logger.debug("Trying to register node (%s) to rockit network" % node_id)

    if namespace and node_id:
        association = models.Association.objects.get(namespace=namespace)

        node, created = models.Node.objects.get_or_create(association=association, aid=node_id)

        if created:
            node.uuid = uuid.uuid4()
            node.save()

            logger.debug("Node (%s) successfully registered to rockit network" % node_id)
            return True
        else:
            logger.warn("Node (%s) has already been created" % node_id)
    else:
        logger.warn("Cannot register if assocation/node_id is empty")

    return False

@task(name='rockit.unregister.node')
def unregister(uuid):
    logger.debug("Trying to unregister node (%s) from rockit network" % uuid)

    if uuid:
        try:
            node = models.Node.objects.get(uuid=uuid)
            node.delete()

            return True
        except models.Node.DoesNotExist:
            logger.warn("Unregister failed. Node (%s) not found" % uuid)
    else:
        logger.warn("Cannot unregister node if uuid is empty")

    return False

@task(name='rockit.settings')
def settings(holder):
    return executors.SettingsExecutor().collect(holder)

@task(name='rockit.mixes')
def mixes(holder):
    return executors.MixesExecutor().collect(holder)

@task(name='rockit.mixes.details')
def mixes_details(identifier, holder):
    return executors.MixesExecutor().collect_details(identifier, holder)

#@celery.decorators.periodic_task(run_every=datetime.timedelta(seconds=30), ignore_result=True)
def scheduler():
    logger.debug("Check for some task to run")
    management.call_command('rockitscheduler')