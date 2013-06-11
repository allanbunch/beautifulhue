from beautifulhue.libs.http import Request

class Config:

    def __init__(self, bridge, user, debug):
        self.bridge = bridge
        self.user = user
        self.debug = debug
        

    def get(self, resource, debug=False):
        """

        """
        
        services = {
            'bridge':{'service':'/config'},
            'system':{'service':''}
        }
        
        request = Request()
        path = 'api/{username}{service}'.format(username=self.user['name'],
                                                service=services[resource['which']]['service'])
        url = 'http://{bridge_ip}/{path}'.format(bridge_ip=self.bridge['ip'],
                                                 path=path)

        status, content = request.get(url)
        if debug:
            return dict(info=status, resource=content)
        else:
            return dict(resource=content)
    
    
    def create(self, resource, debug=False):
        """

        """

        request = Request()
        url = 'http://{bridge_ip}/api'.format(bridge_ip=self.bridge['ip'])
        if resource.has_key('user'):
            resource['user']['username'] = resource['user'].pop('name')
            status, content = request.post(url, resource['user'])
        if debug:
            return dict(info=status, resource=content)
        else:
            return dict(resource=content)


    def update(self, resource, debug=False):
        """

        """

        request = Request()
        path = 'api/{username}/config'.format(username=self.user['name'])
        url = 'http://{bridge_ip}/{path}'.format(bridge_ip=self.bridge['ip'],
                                                 path=path)
        status, content = request.put(url, resource['data']['attr'])
        if debug:
            return dict(info=status, resource=content)
        else:
            return dict(resource=content)
    

    def delete(self, resource, debug=False):
        """

        """

        request = Request()
        if resource.has_key('user'):
            service = 'config/whitelist/{id}'.format(id=resource['user']['name'])
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
    
