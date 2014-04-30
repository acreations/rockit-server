from celery import task

from rockit.plugins.mailout import models

@task(name='mailout.settings')
def settings(holder):
    for server in models.Server.objects.all():
        holder.add(**{
            'key': server.id, 
            'name': 'name',
            'value': 'value'
            })

    return holder

@task(name='mailout.when')
def when(holder):
    return None