# Netbox GED

A plugin designed to faciliate the storage of documents within [NetBox](https://github.com/netbox-community/netbox)  
Re-written from the original [Netbox Documents](https://github.com/jasonyates/netbox-documents/)

## WARNING
THIS PLUGIN IS NOT COMPATIBLE WITH [_NETBOX DOCUMENTS_](https://github.com/jasonyates/netbox-documents/)  
I don't want to break your existing documents, so please don't install this plugin if you have documents stored in the original plugin.

A migration script will, perhaps one day, made available, but for now you will need to manually migrate your documents.


## Features

* Store documents against all NetBox models
* Sort documents with tags and customisable types
* Supports a wide array of common file types


## Compatibility

| NetBox Version | Plugin Version |
|----------------|----------------|
|     3.2+       | 0.2.1          |


## Installation

A working installation of Netbox 3.2+ is required. 3.4+ is recommended.

#### Package Installation from PyPi

Activate your virtual env and install via pip:

```
$ source /opt/netbox/venv/bin/activate
(venv) $ pip install netbox-ged
```

To ensure the Netbox Documents plugin is automatically re-installed during future upgrades, add the package to your `local_requirements.txt` :

```no-highlight
# echo netbox-ged >> local_requirements.txt
```

#### Enable the Plugin

In the Netbox `configuration.py` configuration file add or update the PLUGINS parameter, adding `netbox_documents`:

```python
PLUGINS = [
    'netbox_ged',
]
```

#### Apply Database Migrations

Apply database migrations with Netbox `manage.py`:

```
(venv) $ python manage.py migrate
```

#### Restart Netbox

Restart the Netbox service to apply changes:

```
sudo systemctl restart netbox
```

### Screenshots

Coming soon
