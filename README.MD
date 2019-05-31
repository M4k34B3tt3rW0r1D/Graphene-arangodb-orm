To change installation generate requirements.txt
https://www.idiotinside.com/2015/05/10/python-auto-generate-requirements-txt/
--> commands :
$ pip install pipreqs

$ pipreqs /path/to/project

**This source is free to use. 
Please Stars if you've learned something**


Please note that you should add a file in an external directory to set all your configuration.
For example this project contains a file config.py in
/app/settings/arangodb folder


the config.py contains:
```
DATABASE_CONFIG = {
    'host':'localhost',
    'port':8529,
    'database':'dev',
    'username':'myUsername',
    'password':'MyPassword',
    'verify':True
}

# SERVER 
HOST_CONFIG = {
	'host':'localhost',
	'port':4000
}
```

This allow to have a different configuration between your local machine and your remote server.
please feel free to check https://github.com/mingrammer/python-practices/tree/master/configuration/management
to have some python practices about configuration management.