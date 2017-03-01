URL_BASE = 'https://www.googleapis.com/compute/v1/'


def GenerateConfig(context):
  """Create instance"""

  resources = [{
          'name': vm,
          'type': 'compute.v1.instance',
          'properties': {
              'zone': context.properties['zone'],
              'machineType': context.properties['machineType'],
              'image': URL_BASE + 'projects/albatross-keving-sandbox/global/images/adlib-management-sql-image',
              'networkInterfaces': [{
                'network': URL_BASE + context.env['project'] + '/global/networks/default',
                'accessConfigs': [{
                  'name': 'External NAT',
                  'type': 'ONE_TO_ONE_NAT'
              }]
          }]
      }
  }]
  return {'resources': resources}
