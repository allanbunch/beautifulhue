beautifulhue
============

A Python library for the Philips Hue Lighting System API.

Features
--------
- Complete Philips Hue API v1.0 coverage.
- Consistent method names.
- Designed to get things done.
- JSON/Pyton dictionary resource representation.
- Default response structures are clsely aligned with the official Philips Hue
  API response structures.
- Extensible design.
- Thorough documentation.

Documentation
-------------

###Requirements

- Python 2.6+

###Installation

Via pip:

```bash
pip install beautifulhue
```
or via easy_install:

```bash
easy_install beautifulhue
```
or via source:

```bash
python setup.py install
```

###Bridge
([official reference](http://www.developers.meethue.com/documentation/lights-api))

####Instantiation:

```python
from beautifulhue.api import Bridge

bridge = Bridge(device={'ip':'192.168.1.14'}, user={'name':'newdeveloper'})
# Replace the ip address above with the ip address of your hue bridge.

```

For a more detailed example (including how to create the user if necessary) see the ([wiki](https://github.com/allanbunch/beautifulhue/wiki/Example:-Connect-to-the-Bridge))

###Lights
([official reference](http://www.developers.meethue.com/documentation/lights-api))

####Methods:

####_get_

**Get a single light.**
```python
# Get light number 3.
from beautifulhue.api import Bridge

bridge = Bridge(device={'ip':'192.168.1.14'}, user={'name':'newdeveloper'})
resource = {'which':3}
bridge.light.get(resource)
```

**Get new lights.**
```python
# Get new lights as discovered by the lights.find() method.
from beautifulhue.api import Bridge

bridge = Bridge(device={'ip':'192.168.1.14'}, user={'name':'newdeveloper'})
resource = {'which':'new'}
bridge.light.get(resource)
```

**Get all lights.**
```python
# Get all lights (as defined by Philips Hue documentation).
from beautifulhue.api import Bridge

bridge = Bridge(device={'ip':'192.168.1.14'}, user={'name':'newdeveloper'})
resource = {'which':'all'}
bridge.light.get(resource)
```

Example Response:

```python
{'resource': [
			     {u'name': u'Hue Lamp 1', 'id': 1},
				 {u'name': u'Hue Lamp 2', 'id': 2},
				 {u'name': u'Hue Lamp 3', 'id': 3}
			 ]
}
```

Example Usage:

```python
from beautifulhue.api import Bridge

bridge = Bridge(device={'ip':'192.168.1.14'}, user={'name':'newdeveloper'})
lights = bridge.light.get({'which':'all'})
for light in lights['resource']:
    bridge.light.get({'which':light['id']})
```

**Verbose Mode:**

	- Verbose mode returns a list of expanded, individual light information; the
	same level of deail as when requesting individual lights, as defined in the
	Philips hue documentation.

**Get all lights with verbose light detail.**
```python
# Get all lights with verbose light output.
from beautifulhue.api import Bridge

bridge = Bridge(device={'ip':'192.168.1.14'}, user={'name':'newdeveloper'})
resource = {'which':'all', 'verbose':True}
bridge.light.get(resource)
```

####_find_

**Discover new lights.**
```python
# Find new lights associated with the active bridge.
from beautifulhue.api import Bridge

bridge = Bridge(device={'ip':'192.168.1.14'}, user={'name':'newdeveloper'})
resource = {'which':'new'}
bridge.light.find(resource)
```

####_update_

**Update a light's attributes**
```python
# Update light #3's name.
from beautifulhue.api import Bridge

bridge = Bridge(device={'ip':'192.168.1.14'}, user={'name':'newdeveloper'})
resource = {
    'which':3,
    'data':{
        'attr':{'name':'My Hue Light 3'}
    }
}
bridge.light.update(resource)
```

**Update a light's state.**
```python
# Update light #3's state.
from beautifulhue.api import Bridge

bridge = Bridge(device={'ip':'192.168.1.14'}, user={'name':'newdeveloper'})
resource = {
    'which':3,
    'data':{
        'state':{'on':True, 'ct':222}
    }
}
bridge.light.update(resource)
```


###Groups
([official reference](http://www.developers.meethue.com/documentation/groups-api))

####Methods:

####_get_

**Get a bridge group.**
```python
# Get bridge group 0.
from beautifulhue.api import Bridge

bridge = Bridge(device={'ip':'192.168.1.14'}, user={'name':'newdeveloper'})
resource = {'which':0}
bridge.group.get(resource)
```

**Get all bridge groups.**
```python
# Get all groups.
from beautifulhue.api import Bridge

bridge = Bridge(device={'ip':'192.168.1.14'}, user={'name':'newdeveloper'})
resource = {'which':'all'}
bridge.group.get(resource)
```

**Verbose Mode:**

	- Verbose mode returns a list of expanded, individual group information; the
	same level of deail as when requesting individual groups, as defined in the
	Philips hue documentation.

**Get all groups with verbose group detail.**
```python
# Get all groups with verbose group output.
from beautifulhue.api import Bridge

bridge = Bridge(device={'ip':'192.168.1.14'}, user={'name':'newdeveloper'})
resource = {'which':'all', 'verbose':True}
bridge.group.get(resource)
```

####_update_

**Update a bridge group.**
```python
# Update group 0.
from beautifulhue.api import Bridge

bridge = Bridge(device={'ip':'192.168.1.14'}, user={'name':'newdeveloper'})
resource = {
		       'which':0,
		       'data':{
		           'action':{
		               'on':True,
		               'ct':166,
		               'bri':170
		           }
		       }
		   }
bridge.group.update(resource)
```


###Schedules
([official reference](http://www.developers.meethue.com/documentation/schedules-api-0))

####Methods:

####_get_

**Get a bridge schedule.**
```python
# Get schedule 1.
from beautifulhue.api import Bridge

bridge = Bridge(device={'ip':'192.168.1.14'}, user={'name':'newdeveloper'})
resource = {'which':1}
bridge.schedule.get(resource)
```

**Get all bridge schedules.**
```python
# Get all schedules.
from beautifulhue.api import Bridge

bridge = Bridge(device={'ip':'192.168.1.14'}, user={'name':'newdeveloper'})
resource = {'which':'all'}
bridge.schedule.get(resource)
```

**Verbose Mode:**

	- Verbose mode returns a list of expanded, individual schedule information; the
	same level of deail as when requesting individual schedules, as defined in the
	Philips hue documentation.

**Get all schedules with verbose schedule detail.**
```python
# Get all schedules with verbose schedule output.
from beautifulhue.api import Bridge

bridge = Bridge(device={'ip':'192.168.1.14'}, user={'name':'newdeveloper'})
resource = {'which':'all', 'verbose':True}
bridge.schedule.get(resource)
```

####_create_

**Create a bridge schedule.**
```python
# Create a new schedule.
from beautifulhue.api import Bridge

bridge = Bridge(device={'ip':'192.168.1.14'}, user={'name':'newdeveloper'})
data =  {
    "description": "My wake up alarm!",
    "command": {
        "address": "/api/0/groups/1/action",
        "method": "PUT",
        "body": {
            "on": True
        }
    },
    "time": "2013-06-09T06:30:00"
}
resource = {'which':'my schedule', 'data':data}
bridge.schedule.create(resource)
```

**Update a bridge schedule.**
####_update_
```python
# Update schedule 1's description and time.
from beautifulhue.api import Bridge

bridge = Bridge(device={'ip':'192.168.1.14'}, user={'name':'newdeveloper'})
data =  {
    "description": "My updated alarm!",
    "time": "2013-06-09T05:30:00"
}
resource = {'which':1, 'data':data}
bridge.schedule.update(resource)
```

####_delete_

**Delete a bridge schedule.**
```python
# Delete schedule 1.
from beautifulhue.api import Bridge

bridge = Bridge(device={'ip':'192.168.1.14'}, user={'name':'newdeveloper'})
resource = {'which':1}
bridge.schedule.delete(resource)
```

###Configuration
([official reference](http://www.developers.meethue.com/documentation/configuration-api))

####Methods:

####_get_

**Get bridge configuration.**
```python
# Get bridge config.
from beautifulhue.api import Bridge

bridge = Bridge(device={'ip':'192.168.1.14'}, user={'name':'newdeveloper'})
resource = {'which':'bridge'}
bridge.config.get(resource)
```

**Get system configuration.**
```python
# Get system config.
from beautifulhue.api import Bridge

bridge = Bridge(device={'ip':'192.168.1.14'}, user={'name':'newdeveloper'})
resource = {'which':'system'}
bridge.config.get(resource)
```

####_create_

**Create a bridge configuration object.**
```python
# Create a new bridge user.
from beautifulhue.api import Bridge

bridge = Bridge(device={'ip':'192.168.1.14'}, user={'name':'newdeveloper'})
resource = {'user':{"devicetype": "beautifulhue", "name": "1234567890"}}
bridge.config.create(resource)
```

####_update_

**Update bridge configuration attributes.**
```python
resource = {
    'data':{
        'attr':{
            'name':'My Bridge Name'
        }
    }
}
bridge.config.update(resource)
```

####_delete_

**Delete a bridge configuration object.**
```python
# Delete a bridge user.
from beautifulhue.api import Bridge

bridge = Bridge(device={'ip':'192.168.1.14'}, user={'name':'newdeveloper'})
resource = {'user':{"name": "1234567890"}}
bridge.config.delete(resource)
```

###Portal

####Instantiation:

```python
from beautifulhue.api import Portal
```

####Methods:

####_get_

**Get hue portal data.**
```python
from beautifulhue.api import Portal

portal = Portal()
portal.get()
```

