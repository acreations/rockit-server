from celery import task

from rockit.plugins.mailout import models

@task(name='mailout.settings')
def settings(holder):
    holder.add(**{
      'key': server.id,
      'name': 'name',
      'value': 'value'
    })

    return holder

@task(name='mailout.mixes')
def mixes(holder):
    return None