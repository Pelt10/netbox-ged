from extras.plugins import PluginConfig


class NetboxGED(PluginConfig):
    name = 'netbox_ged'
    verbose_name = 'Document Storage'
    description = 'Manage documents in Netbox'
    version = '0.2.0'
    author = 'Pelt10'
    author_email = 'contact@lethiec.me'
    min_version = '3.2.0'
    base_url = 'documents'


config = NetboxGED
