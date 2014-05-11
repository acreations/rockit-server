from celery import task

from rockit.plugins.razberry import actions
from rockit.plugins.razberry import executors
from rockit.plugins.razberry import models
from rockit.plugins.razberry import resolvers
from rockit.plugins.razberry import services

@task(name='razberry.node.commands')
def node_commands(identifier, holder):
    instances = services.RazberryService().retrieve_instances(identifier)

    if instances:
        for key, instance in instances.items():
            builder = actions.ActionBuilder(instance['commandClasses'])
            builder.filter_actions_by_command_classes(identifier, holder)

    return holder

@task(name='razberry.node.command.value')
def node_command_value(identifier, command_id):
    service = services.RazberryService()
    command = service.retrieve(command_id)

    if command:
        data = resolvers.ValueResolver().resolve_command_value(command)

        if data:
            return service.retrieve("%s.%s" % (command_id, data))
            
    return None

@task(name='razberry.node.command.update.value')
def node_command_update_value(identifier, command_id, value):
    service = services.RazberryService()
    command = service.retrieve(command_id)

    if command:
        updateTime = command['data']['updateTime']
        service.update(command_id, value)

        data = service.data(updateTime)

        return node_command_value(identifier, command_id)

    return None

@task(name='razberry.node.detailed')
def node_detailed(identifier, holder):
    node = models.Node.objects.get(device_id=identifier)
    version = models.NodeVersion.objects.get(node=node)

    holder.add(**to_kwargs('device_type', node.device_type))
    holder.add(**to_kwargs('manufacturer_name', node.manufacturer_name))
    holder.add(**to_kwargs('manufacturer_id', node.manufacturer_id))

    holder.add(**to_kwargs('isListening', node.listening))
    holder.add(**to_kwargs('routing', node.routing))
    holder.add(**to_kwargs('beaming', node.beaming))
    holder.add(**to_kwargs('awaken', node.awaken))
    holder.add(**to_kwargs('failed', node.failed))

    holder.add(**to_kwargs('sdk', version.sdk))
    holder.add(**to_kwargs('application', version.application))
    holder.add(**to_kwargs('zw_library', version.zw_library))
    holder.add(**to_kwargs('zw_protocol', version.zw_protocol))

    return holder

@task(name='razberry.settings')
def settings(holder):

    for setting in models.Setting.objects.all():
        holder.add(**{
            'key': setting.id,
            'name': setting.name,
            'value': setting.value,
            'readonly': setting.readonly
            })

    return holder

@task(name='razberry.mixes')
def mixes(holder):
    return executors.MixesExecutor().collect(holder)

@task(name='razberry.mixes.details')
def mixes_details(identifier, holder):
    return executors.MixesExecutor().collect_details(identifier, holder)

def to_kwargs(title, value):
    return {
        'title': title,
        'value': value
    }