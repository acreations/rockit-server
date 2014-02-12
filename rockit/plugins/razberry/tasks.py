from celery import task

from rockit.plugins.razberry import models

@task(name='razberry.node.detailed')
def node_detailed(identifier, holder):
    node = models.Node.objects.get(device_id=identifier)
    version = models.NodeVersion.objects.get(node=node)

    holder.add_details('device_type', node.device_type)
    holder.add_details('manufacturer_name', node.manufacturer_id)
    holder.add_details('manufacturer_id', node.manufacturer_name)

    holder.add_details('isListening', node.listening)
    holder.add_details('routing', node.routing)
    holder.add_details('beaming', node.beaming)
    holder.add_details('awaken', node.awaken)
    holder.add_details('failed', node.failed)

    holder.add_details('sdk', version.sdk)
    holder.add_details('application', version.application)
    holder.add_details('zw_library', version.zw_library)
    holder.add_details('zw_protocol', version.zw_protocol)

    return holder