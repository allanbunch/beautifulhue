from _portal import Portal

class Bridge():
    
    def __init__(self, device, user, debug=False):
        from _config import Config
        from _group import Group
        from _light import Light
        from _scene import Scene
        from _schedule import Schedule
    
        self.config = Config(device, user, debug)
        self.group = Group(device, user, debug)
        self.light = Light(device, user, debug)
        self.schedule = Schedule(device, user, debug)
        self.scene = Scene(device, user, debug)
        
class Portal(Portal):
    
    pass
