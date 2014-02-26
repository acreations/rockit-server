from celery import task

from rockit.plugins.razberry import actions
from rockit.plugins.razberry import models
from rockit.plugins.razberry import services

@task(name='razberry.node.commands')
def node_commands(identifier, holder):
    instances = services.RazberryService().retrieve_instances(identifier)

    if instances:
        for key, instance in instances.items():
            builder = actions.ActionBuilder(instance['commandClasses'])
            builder.filter_actions_by_command_classes(identifier, holder)

    return holder

@task(name='razberry.node.detailed')
def node_detailed(identifier, holder):
    node = models.Node.objects.get(device_id=identifier)
    version = models.NodeVersion.objects.get(node=node)

    holder.add_detail('device_type', node.device_type)
    holder.add_detail('manufacturer_name', node.manufacturer_name)
    holder.add_detail('manufacturer_id', node.manufacturer_id)

    holder.add_detail('isListening', node.listening)
    holder.add_detail('routing', node.routing)
    holder.add_detail('beaming', node.beaming)
    holder.add_detail('awaken', node.awaken)
    holder.add_detail('failed', node.failed)

    holder.add_detail('sdk', version.sdk)
    holder.add_detail('application', version.application)
    holder.add_detail('zw_library', version.zw_library)
    holder.add_detail('zw_protocol', version.zw_protocol)

    return holder

@task(name='razberryx.settings')
def settings(holder):

    return holder