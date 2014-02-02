from celery import task
from celery.utils.log import get_task_logger

from rockit.foundation.core.models import Node

import uuid

logger = get_task_logger(__name__)

@task(name='rockit-register-node')
def register(association, aid):
    logger.debug("Trying to register node (%s) to rockit network" % aid)

    if association and aid:
        node, created = Node.objects.get_or_create(association=association, aid=aid)

        if created:
            node.uuid = uuid.uuid4()
            node.save()

            logger.debug("Node (%s) successfully registered to rockit network" % aid)
            return True
        else:
            logger.warn("Node (%s) has already been created" % aid)
    else:
        logger.warn("Cannot register if assocation/aid is empty")

    return False

@task(name='rockit-unregister-node')
def unregister(uuid):
    logger.debug("Trying to unregister node (%s) from rockit network" % uuid)
