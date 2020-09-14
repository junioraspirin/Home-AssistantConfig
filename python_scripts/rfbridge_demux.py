d = { '740E01':['stereopower','ON','false'],
      '740E04':['stereolight','ON','false'],
      '740E05':['stereobrightp','ON','false'],
      '740E06':['stereobrightm','ON','false'],
      '740E07':['stereo100','ON','false'],
      '740E08':['stereo50','ON','false'],
      '740E09':['stereo25','ON','false'],
      '740E0B':['stereomodep','ON','false'],
      '740E11':['stereomodem','ON','false'],
      '740E0D':['stereospeedm','ON','false'],
      '740E0F':['stereospeedp','ON','false']
    }

p = data.get('payload')

if p is not None:
  if p in d.keys():
    service_data = {'topic':'home/{}'.format(d[p][0]), 'payload':'{}'.format(d[p][1]), 'qos':0, 'retain':'{}'.format(d[p][2])}
  else:
    service_data = {'topic':'home/unknown', 'payload':'{}'.format(p), 'qos':0, 'retain':'false'}
    logger.warning('<rfbridge_demux> Received unknown RF command: {}'.format(p))
  hass.services.call('mqtt', 'publish', service_data, False)