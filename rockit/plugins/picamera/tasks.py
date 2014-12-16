from celery import task

from rockit.plugins.mailout import models

@task(name='picamera.settings')
def settings(holder):
    for setting in models.Setting.objects.all():
      holder.add(**{
        'key': setting.id,
        'name': setting.name,
        'value': setting.value
      })

    return holder

@task(name='picamera.mixes')
def mixes(holder):
    return None