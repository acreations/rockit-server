from celery import task

from rockit.plugins.mailout import models

@task(name='mailout.settings')
def settings(holder):
    for server in models.Server.objects.all():
        holder.add_simple(server.id, 'name', 'value')

    return holder