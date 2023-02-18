import django_tables2 as tables

from netbox.tables import NetBoxTable, columns
from .models import Document, DocumentType

DOCUMENT_LINK = """
<a href="{% url 'plugins:netbox_ged:document' pk=record.pk %}">{% firstof record.name record.filename %}</a> (<a href="{{record.document.url}}" target="_blank">View Document</a>)
"""


class DocumentTable(NetBoxTable):
    name = tables.TemplateColumn(template_code=DOCUMENT_LINK)
    document_type = columns.ColoredLabelColumn()

    tags = columns.TagColumn(
        url_name='plugins:netbox_ged:document_list'
    )

    class Meta(NetBoxTable.Meta):
        model = Document
        fields = ('pk', 'id', 'name', 'document_type',  'size', 'filename', 'comments', 'actions', 'created', 'last_updated', 'tags')
        default_columns = ('name', 'document_type', 'tags')


class DocumentTypeTable(NetBoxTable):
    name = tables.Column(
        linkify=True,
    )
    color = columns.ColorColumn()

    class Meta(NetBoxTable.Meta):
        model = DocumentType
        fields = ('pk', 'id', 'name', 'color')
        default_columns = ('name', 'color')
