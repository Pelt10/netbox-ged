from netbox.views import generic
from .filtersets import DocumentTypeFilterSet, DocumentFilterSet
from .forms import DocumentTypeFilterForm, DocumentTypeForm, DocumentForm, DocumentFilterForm, DocumentLinkForm, \
    DocumentCreateForm
from .models import Document, DocumentType, DocumentLink
from .tables import DocumentTypeTable, DocumentTable


# Document
class DocumentView(generic.ObjectView):
    queryset = Document.objects.all()


class DocumentListView(generic.ObjectListView):
    queryset = Document.objects.all()
    table = DocumentTable
    filterset = DocumentFilterSet
    filterset_form = DocumentFilterForm


class DocumentEditView(generic.ObjectEditView):
    queryset = Document.objects.all()
    form = DocumentForm


class DocumentDeleteView(generic.ObjectDeleteView):
    queryset = Document.objects.all()


# DocumentType
class DocumentTypeView(generic.ObjectView):
    queryset = DocumentType.objects.all()


class DocumentTypeListView(generic.ObjectListView):
    queryset = DocumentType.objects.all()
    table = DocumentTypeTable
    filterset = DocumentTypeFilterSet
    filterset_form = DocumentTypeFilterForm


class DocumentTypeEditView(generic.ObjectEditView):
    queryset = DocumentType.objects.all()
    form = DocumentTypeForm


class DocumentTypeDeleteView(generic.ObjectDeleteView):
    queryset = DocumentType.objects.all()


class DocumentLinkEditView(generic.ObjectEditView):
    queryset = DocumentLink.objects.all()
    form = DocumentLinkForm


class DocumentLinkDeleteView(generic.ObjectDeleteView):
    queryset = DocumentLink.objects.all()


# View to create a new document and document link in one step
class DocumentCreateView(generic.ObjectEditView):
    queryset = Document.objects.all()
    form = DocumentCreateForm

    def get_initial(self):
        initial = super().get_initial()
        initial['document_type'] = DocumentType.objects.first()
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'].fields['document_type'].queryset = DocumentType.objects.all()
        return context
