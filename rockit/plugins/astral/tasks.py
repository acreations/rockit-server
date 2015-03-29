from celery import task
from celery.execute import send_task
from celery.signals import celeryd_init
from celery.signals import celeryd_after_setup
from celery.utils.log import get_task_logger

@celeryd_after_setup.connect
def init(sender, instance, **kwargs):
    send_task('rockit.hey', ['astral'])

@task(ignore_result=True)
def hey():
    logger = hey.get_logger()

    send_task('rockit.register.association', kwargs={
        'name': 'Astral',
        'namespace': 'rockit.plugins.astral',
        'description': 'Settings for astral to calculate Sunrise and Sunset',
        'entry': 'astral'
    })

@task(name='astral.settings')
def settings(holder):
    return holder

@task(name='astral.mixes')
def mixes(holder):
    return None