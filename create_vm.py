COMPUTE_URL_BASE = 'https://www.googleapis.com/compute/v1/'


def GenerateConfig(context):
  """Create instance"""

  resources = [{
          'name': vm,
          'type': 'compute.v1.instance',
          'properties': {
              'zone': context.properties['zone'],
              'machineType': context.properties['machineType'],
              'image': COMPUTE_URL_BASE, + 'projects/albatross-keving-sandbox/global/images/adlib-management-sql-image',
      }
  }]
  return {'resources': resources}
