from beautifulhue.libs.http import Request

class Schedule:
    """
    """
    

    def __init__(self, bridge, user, debug):
        self.bridge = bridge
        self.user = user
        self.debug = debug
        

    def get(self, resource, debug=False):
        """
        
        """
        
        request = Request()
        services = {
            'all':{'service':'schedules'}
        }

        if (isinstance(resource['which'], int)):
            resource['id'] = resource['which']
            resource['which'] = 'one'
        if (resource['which'] == 'one'):
            services['one'] = {'service':'schedules/{id}'.format(id=resource['id'])}
        
        service = services[resource['which']]['service']
        path = 'api/{username}/{service}'.format(
                                               username=self.user['name'],
                                               service=service
                                           )
        url = 'http://{bridge_ip}/{path}'.format(bridge_ip=self.bridge['ip'],
                                                 path=path)
        status, content = request.get(url)
        if service == 'schedules':
            schedules = []
            for (k, v) in content.items():
                v['id'] = int(k)
                schedules.append(v)
            if resource.has_key('verbose') and resource['verbose']:
                _schedules = []
                for schedule in schedules:
                    path = 'api/{username}/schedules/{id}'.format(
                                                                  username=self.user['name'],
                                                                  id=schedule['id']
                                                              )
                    url = 'http://{bridge_ip}/{path}'.format(bridge_ip=self.bridge['ip'],
                                                     path=path)
                    status, content = request.get(url, resource)
                    _schedules.append(content)
                content = _schedules
            else:
                content = schedules
        
        if debug:
            return dict(info=status, resource=content)
        else:
            return dict(resource=content)
    
    
    def create(self, resource, debug=False):
        """

        """

        request = Request()
        path = 'api/{username}/schedules'.format(username=self.user['name'])
        url = 'http://{bridge_ip}/{path}'.format(bridge_ip=self.bridge['ip'],
                                                 path=path)
        resource['data']['name'] = resource['which']
        status, content = request.post(url, resource['data'])
        if debug:
            return dict(info=status, resource=content)
        else:
            return dict(resource=content)


    def update(self, resource, debug=False):
        """

        """

        request = Request()
        service = 'schedules/{id}'.format(id=resource['which'])
        path = 'api/{username}/{service}'.format(
                                               username=self.user['name'],
                                               service=service
                                           )
        url = 'http://{bridge_ip}/{path}'.format(bridge_ip=self.bridge['ip'],
                                                 path=path)
        
        status, content = request.put(url, resource['data'])
        if debug:
            return dict(info=status, resource=content)
        else:
            return dict(resource=content)
    

    def delete(self, resource, debug=False):
        """

        """

        request = Request()
        service = 'schedules/{id}'.format(id=resource['which'])
        path = 'api/{username}/{service}'.format(
                                               username=self.user['name'],
                                               service=service
                                           )
        url = 'http://{bridge_ip}/{path}'.format(bridge_ip=self.bridge['ip'],
                                                 path=path)
        
        status, content = request.delete(url)
        if debug:
            return dict(info=status, resource=content)
        else:
            return dict(resource=content)
    
