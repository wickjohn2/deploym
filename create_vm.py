URL_BASE = 'https://www.googleapis.com/compute/v1/'


def GenerateConfig(context):
  """Create instance"""

  zone = context.properties['zone']
  machineType = context.properties['machineType']
  
  resources = [{
          'name': 'management-sql-'+ context.env['deployment'],
          'type': 'compute.v1.instance',
          'properties': {
              'zone': zone,
              'machineType': machineType,
              'image': URL_BASE + 'projects/albatross-keving-sandbox/global/images/adlib-management-sql-image',
              'networkInterfaces': [{
                'network': URL_BASE + context.env['project'] + '/global/networks/default',
          }]
      }
  }]
  return {'resources': resources}
