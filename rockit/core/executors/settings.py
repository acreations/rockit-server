
from rockit.core import models

class SettingsExecutor(object):

    def collect(self, holder):
        '''
        Collect settings
        '''
        for setting in models.Setting.objects.all():
            holder.add(**{
                'key': setting.id,
                'name': setting.name,
                'value': setting.value
                })

        return holder