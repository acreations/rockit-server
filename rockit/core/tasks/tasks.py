
from celery import task
from celery.execute import send_task
from celery.utils.log import get_task_logger

from rockit.core import models
from rockit.core import executors

import uuid

logger = get_task_logger(__name__)

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
    return None #executors.MixesExecutor().collect_details(identifier, holder)

@task(name='rockit.notify.when')
def notify_when(entry, identifier):

    association = models.Association.objects.get(entry=entry)

    try:
        when = models.ActionWhen.objects.get(target=association, identifier=identifier)
        then = models.ActionThen.objects.filter(holder=when.holder)

        for item in then:
            send_task("%s.mixes.then.run" % item.target.entry, [item.identifier])
    except models.ActionWhen.DoesNotExist:
        models.ActionFailure.objects.get_or_create(target=association, identifier=identifier, holder='when')
