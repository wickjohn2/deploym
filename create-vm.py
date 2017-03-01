def GenerateConfig(context):
  
  resources {
    'type': 'compute.v1.instance'
    'name': context.name
    'properties': {
          'zone': context.properties['zone'],
          'machineType': context.properties['machinetype'],
          'image': context.properties['image']
    }
  }
  return {'resources': resources}
      