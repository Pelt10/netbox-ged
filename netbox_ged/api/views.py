from netbox.api.viewsets import NetBoxModelViewSet

from .serializers import DocumentSerializer, DocumentTypeSerializer
from ..filtersets import DocumentTypeFilterSet, DocumentFilterSet
from ..models import DocumentType, Document


class DocumentViewSet(NetBoxModelViewSet):
    queryset = Document.objects.prefetch_related('tags')
    serializer_class = DocumentSerializer
    filterset_class = DocumentFilterSet


class DocumentTypeViewSet(NetBoxModelViewSet):
    queryset = DocumentType.objects.prefetch_related('tags')
    serializer_class = DocumentTypeSerializer
    filterset_class = DocumentTypeFilterSet
