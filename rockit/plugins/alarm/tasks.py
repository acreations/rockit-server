import time

from celery import task

from rockit.plugins.alarm import executors

@task(name='alarm.settings')
def settings(holder):
    return holder

@task(name='alarm.mixes')
def mixes(holder):

    holder.add_when(**{ 'identifier': 'alarm', 'name': 'Alarm' })
    return holder

@task(name='alarm.mixes.details')
def mixes_details(identifier, holder):

    holder.add_post(**{
        'identifier': 'alarm',
        'type': 'alarm',
        'label': 'Alarm',
        'required': True
    })

    #holder.add_post(**{
    #    'identifier': 'alarm-repeat',
    #    'type': 'checkbox',
    #    'label': 'Repeat',
    #    'required': False,
    #    'value': ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    #})

    return holder

@task(name='alarm.mixes.when.validate')
def mixes_when_validate(identifier, criterias, holder):

    if criterias:
        criteria = criterias[0]

        if criteria['id'] == "alarm":
            try:
                time.strptime(criteria['value'], '%H:%M')
                return holder
            except ValueError:
                holder.add_error(criteria['id'], 'Criteria value does not have a time format')

        else:
            holder.add_error(criteria['id'], 'Unknown id')
    else:
        holder.add_error('alarm', 'Value must be provided')

    return holder
