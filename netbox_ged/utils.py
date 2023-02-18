
def file_upload(instance, filename):

    """
    Return a path for uploading image attachments.
    Adapted from netbox/extras/utils.py
    """
    path = 'netbox-ged/'

    # Rename the file to the provided name, if any. Attempt to preserve the file extension.
    extension = filename.rsplit('.')[-1].lower()
    if instance.name and extension in ['bmp', 'gif', 'jpeg', 'jpg', 'png', 'pdf', 'txt', 'doc', 'docx', 'xls', 'xlsx', 'xlsm']:
        filename = '.'.join([instance.name, extension])
    elif instance.name:
        filename = instance.name

    return '{}{}_{}'.format(path, instance.__class__.__name__, filename)