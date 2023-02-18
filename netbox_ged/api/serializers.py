from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import Document, DocumentType, DocumentLink


class DocumentLinkSerializer(WritableNestedSerializer):
    class Meta:
        model = DocumentLink
        fields = ['id', 'document', 'content_type', 'object_id']


# Site Document Serializer
class DocumentSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_ged-api:document-detail'
    )
    relative_objects = DocumentLinkSerializer(many=True, read_only=True)

    class Meta:
        model = Document
        fields = (
            'id', 'url', 'display', 'relative_objects', 'name', 'document', 'document_type', 'filename', 'comments', 'tags',
            'custom_fields', 'created', 'last_updated',
        )


# Site Document Type Serializer
class DocumentTypeSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='plugins-api:netbox_ged-api:documenttype-detail')

    class Meta:
        model = DocumentType
        fields = (
            'id', 'url', 'display', 'name', 'color', 'tags', 'custom_fields', 'created',
            'last_updated',
        )

