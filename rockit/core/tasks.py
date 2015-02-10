
from celery import task
from celery.execute import send_task
from celery.utils.log import get_task_logger

from rockit.core import models
from rockit.core import executors

import uuid

logger = get_task_logger(__name__)

@task(name='rockit.register.node')
def register(namespace, node_id):
    logger.debug('Trying to register node (%s) to rockit network' % node_id)

    if namespace and node_id:
        association = models.Association.objects.get(namespace=namespace)

        node, created = models.Node.objects.get_or_create(association=association, aid=node_id)

        if created:
            node.uuid = uuid.uuid4()
            node.save()

            logger.debug('Node (%s) successfully registered to rockit network' % node_id)

            return node.uuid
        else:
            logger.warn('Node (%s) has already been created' % node_id)
    else:
        logger.warn('Cannot register if assocation/node_id is empty')

    return None

@task(name='rockit.unregister.node')
def unregister(uuid):
    logger.debug('Trying to unregister node (%s) from rockit network' % uuid)

    if uuid:
        try:
            node = models.Node.objects.get(uuid=uuid)
            node.delete()

            return True
        except models.Node.DoesNotExist:
            logger.warn('Unregister failed. Node (%s) not found' % uuid)
    else:
        logger.warn('Cannot unregister node if uuid is empty')

    return False

@task(name='rockit.settings')
def settings(holder):
    return executors.SettingsExecutor().collect(holder)

@task(name='rockit.mixes')
def mixes(holder):
    return executors.MixesExecutor().collect(holder)

@task(name='rockit.mixes.when.validate')
def mixes_when_validate(identifier, criterias, holder):
    return executors.MixesExecutor().validate(criterias, holder)

@task(name='rockit.mixes.details')
def mixes_details(identifier, holder):
    return executors.MixesExecutor().collect_details(identifier, holder)

@task(name='rockit.notify.when')
def notify_when(entry, identifier):

    association = models.Association.objects.get(entry=entry)

    try:
        when = models.ActionWhen.objects.get(target=association, identifier=identifier)
        then = models.ActionThen.objects.filter(holder=when.holder)

        for item in then:
            send_task("%s.mixes.then.run" % item.target.entry, [item.identifier])
    except models.ActionWhen.DoesNotExist:
        models.ActionFailure.objects.get_or_create(target=association, identifier=identifier, 'when')
