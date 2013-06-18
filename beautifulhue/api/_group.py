from beautifulhue.libs.http import Request

class Group:

    def __init__(self, bridge, user, debug):
        self.bridge = bridge
        self.user = user
        self.debug = debug

    def get(self, resource, debug=False):
        """

        """
        
        request = Request()
        services = {
            'all':{'service':'groups'}
        }

        if (isinstance(resource['which'], int)):
            resource['id'] = resource['which']
            resource['which'] = 'one'
        if (resource['which'] == 'one'):
            services['one'] = {'service':'groups/{id}'.format(id=resource['id'])}
        
        service = services[resource['which']]['service']
        path = 'api/{username}/{service}'.format(
                                               username=self.user['name'],
                                               service=service
                                           )
        url = 'http://{bridge_ip}/{path}'.format(bridge_ip=self.bridge['ip'],
                                                 path=path)
        status, content = request.get(url, resource)
        if service == 'groups':
            groups = []
            for (k, v) in content.items():
                v['id'] = int(k)
                groups.append(v)
            if resource.has_key('verbose') and resource['verbose']:
                _groups = []
                for group in groups:
                    path = 'api/{username}/groups/{id}'.format(
                                                                  username=self.user['name'],
                                                                  id=group['id']
                                                              )
                    url = 'http://{bridge_ip}/{path}'.format(bridge_ip=self.bridge['ip'],
                                                     path=path)
                    status, content = request.get(url, resource)
                    _groups.append(content)
                content = _groups
            else:
                content = groups
        if debug:
            return dict(info=status, resource=content)
        else:
            return dict(resource=content)

    def update(self, resource, debug=False):
        """

        """

        request = Request()
        if (resource['data'].has_key('name')):
            service = 'groups/{id}'.format(id=resource['which'])
        elif (resource['data'].has_key('action')):
            service = 'groups/{id}/action'.format(id=resource['which'])
        else:
            raise Exception('Unknown data type.')
        path = 'api/{username}/{service}'.format(
                                               username=self.user['name'],
                                               service=service
                                           )
        url = 'http://{bridge_ip}/{path}'.format(bridge_ip=self.bridge['ip'],
                                                 path=path)
        
        status, content = request.put(url, resource['data']['action'])
        if debug:
            return dict(info=status, resource=content)
        else:
            return dict(resource=content)
