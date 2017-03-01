def GenerateConfig(context):
  
  resources = [{
    'type': 'compute.v1.instance',
    'name': 'vm-' + context.properties['function'],
    'properties': {
          'zone': context.properties['zone'],
          'machine-type': context.properties['machinetype'],
          'image': context.properties['image'],
    }
  }]
  return {'resources': resources}
      
