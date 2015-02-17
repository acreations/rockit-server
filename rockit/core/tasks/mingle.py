import celery

from celery import task
from celery.execute import send_task

from datetime import timedelta

from rockit.core import models

@task(name='rockit.hey', ignore_result=True, countdown=5)
def hey(entry):
    logger = hey.get_logger()

    logger.debug('Received hello from %s' % entry)

    if entry:
        mingle, created = models.Hello.objects.get_or_create(entry=entry)

        if not created:
            """
            Reset if exist in database
            """
            mingle.done = False
            mingle.save()

        logger.debug('Saved hello from %s' % entry)
    else:
        logger.warn("Did not receive a proper hello")

@celery.decorators.periodic_task(name='rockit.hey.back', run_every=timedelta(seconds=120), ignore_result=True, bind=True)
def hey_back(self):
    logger = self.get_logger()

    logger.debug("Check if someone said hello")

    for mingle in models.Hello.objects.filter(done=False):
        """
        Time to mingle back
        """
        logger.debug("Trying to say hello back to %s" % mingle.entry)
        send_task('rockit.plugins.%s.tasks.hey' % mingle.entry)

        mingle.done = True
        mingle.save()