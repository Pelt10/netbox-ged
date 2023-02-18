from netbox.search import SearchIndex
from .models import Document
from django.conf import settings

# If we run NB 3.4+ register search indexes 
if settings.VERSION >= '3.4.0':
    class DocumentIndex(SearchIndex):
        model = Document
        fields = (
            ("name", 100),
            ("document_type__name", 500),
        )


    # Register indexes
    indexes = [DocumentIndex]
