from beautifulhue.libs.http import Request

class Portal:
    """
    @status: Done
    """

    def __init__(self, debug=False):
        self.debug = debug

    def get(self, debug=False):
        """
        @status: Done
        """

        request = Request()
        url = 'http://www.meethue.com/api/nupnp'
        status, content = request.get(url)
        
        if debug:
            return dict(info=status, resource=content)
        else:
            return dict(resource=content)
