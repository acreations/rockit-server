from celery import task

@task(name='astral.settings')
def settings(holder):
    return holder

@task(name='astral.mixes')
def mixes(holder):
    return None