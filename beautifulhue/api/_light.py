from beautifulhue.libs.http import Request

class Light:

    def __init__(self, bridge, user, debug):
        self.bridge = bridge
        self.user = user
        self.debug = debug
        
    def get(self, resource, debug=False):
        """
        @summary: Get all lights, get new lights, or get a specific light as\
                  determined by the resource object.

        @TODO: Fix resource variable scope issue that manifests when making\
               multiple light.get(resource) calls.
        """
        
        request = Request()
        services = {
            'all':{'service':'lights'},
            'new':{'service':'lights/new'}
        }
        if (isinstance(resource['which'], int)):
            resource['id'] = resource['which']
            resource['which'] = 'one'
        if (resource['which'] == 'one'):
            services['one'] = {'service':'lights/{id}'.format(id=resource['id'])}
        service = services[resource['which']]['service']
        path = 'api/{username}/{service}'.format(
                                                    username=self.user['name'],
                                                    service=service
                                                )
        url = 'http://{bridge_ip}/{path}'.format(bridge_ip=self.bridge['ip'],
                                                 path=path)

        status, content = request.get(url, resource)
        if service == 'lights':
            lights = []
            for (k, v) in content.items():
                v['id'] = int(k)
                lights.append(v)
            if resource.has_key('verbose') and resource['verbose']:
                _lights = []
                for light in lights:
                    path = 'api/{username}/lights/{id}'.format(
                                                                  username=self.user['name'],
                                                                  id=light['id']
                                                              )
                    url = 'http://{bridge_ip}/{path}'.format(bridge_ip=self.bridge['ip'],
                                                     path=path)
                    status, content = request.get(url, resource)
                    _lights.append(content)
                content = _lights
            else:
                content = lights


        if debug:
            return dict(info=status, resource=content)
        else:
            return dict(resource=content)


    def find(self, resource, debug=False):
        """
        @summary: Search for new lights.
        """
        
        request = Request()
        
        services = {
            'new':{'service':'lights'}
        }
        
        service = services[resource['which']]['service']
        path = 'api/{username}/{service}'.format(
                                               username=self.user['name'],
                                               service=service
                                           )
        url = 'http://{bridge_ip}/{path}'.format(bridge_ip=self.bridge['ip'],
                                                 path=path)

        status, content = request.post(url)
        if debug:
            return dict(info=status, resource=content)
        else:
            return dict(resource=content)


    def update(self, resource, debug=False):
        """
        @summary: Rename lights, or set a light's state, as determined by the\
                  resource object.
        """

        request = Request()
        if (resource['data'].has_key('attr')):
            service = 'lights/{id}'.format(id=resource['which'])
            data = resource['data']['attr']
        elif (resource['data'].has_key('state')):
            service = 'lights/{id}/state'.format(id=resource['which'])
            data = resource['data']['state']
        else:
            raise Exception('Unknown data type.')
        path = 'api/{username}/{service}'.format(
                                               username=self.user['name'],
                                               service=service
                                           )
        url = 'http://{bridge_ip}/{path}'.format(bridge_ip=self.bridge['ip'],
                                                 path=path)
        
        status, content = request.put(url, data)
        if debug:
            return dict(info=status, resource=content)
        else:
            return dict(resource=content)
