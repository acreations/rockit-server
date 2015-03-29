import celery

from celery import task
from celery.execute import send_task
from celery.utils.log import get_task_logger

from django.conf import settings
from django.core.cache import cache
from django.db import transaction, IntegrityError

from datetime import timedelta

from rockit.core import models

LOCK_EXPIRE = 60 * 5 # Lock expires in 5 minutes

logger = get_task_logger(__name__)

@task(name='rockit.hey', ignore_result=True, countdown=5)
def hey(entry):
    if entry:
        """
        If entry is not empty, process it
        """
        lock_id = '{0}-lock'.format('rockit.hey')

        # cache.add fails if if the key already exists
        acquire_lock = lambda: cache.add(lock_id, 'true', LOCK_EXPIRE)
        # memcache delete is very slow, but we have to use it to take
        # advantage of using add() for atomic locking
        release_lock = lambda: cache.delete(lock_id)

        logger.debug('Received hello from %s' % entry)

        if acquire_lock():
            try:

                mingle, created = models.Hello.objects.get_or_create(entry=entry)

                if not created:
                    """
                    Reset if exist in database
                    """
                    mingle.done = False

                mingle.save()

            finally:
                release_lock()

            return True
        else:
            logger.debug(
                'Hello message is being proccessed by another worker')
    else:
        logger.error('Entry cannot be empty')

    return False


@celery.decorators.periodic_task(name='rockit.hey.back', run_every=timedelta(seconds=120), ignore_result=True, bind=True)
def hey_back(self):
    logger = self.get_logger()

    logger.debug("Check if someone said hello")

    for mingle in models.Hello.objects.filter(done=False, date_modified__gt=settings.STARTUP_TIME):
        """
        Time to mingle back
        """
        logger.debug("Trying to say hello back to %s" % mingle.entry)
        send_task('rockit.plugins.%s.tasks.hey' % mingle.entry)

        mingle.delete()