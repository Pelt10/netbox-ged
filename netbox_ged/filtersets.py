from netbox.filtersets import NetBoxModelFilterSet
from .models import Document, DocumentType
from django.db.models import Q


class DocumentFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Document
        fields = ('id', 'name', 'document_type')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value) |
            Q(document__icontains=value)
        )


class DocumentTypeFilterSet(NetBoxModelFilterSet):

        class Meta:
            model = DocumentType
            fields = ('id', 'name')

        def search(self, queryset, name, value):
            if not value.strip():
                return queryset
            return queryset.filter(
                Q(name__icontains=value) |
                Q(slug__icontains=value)
            )