from django.contrib.contenttypes.models import ContentType
from django.forms import CharField, IntegerField
from extras.utils import FeatureQuery
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms import TagFilterField, CommentField, DynamicModelMultipleChoiceField, DynamicModelChoiceField, \
    ContentTypeChoiceField
from .models import Document, DocumentType, DocumentLink


# Document Form & Filter Form
class DocumentForm(NetBoxModelForm):
    comments = CommentField()
    document_type = DynamicModelChoiceField(
        queryset=DocumentType.objects.all(),
        required=True,
    )

    class Meta:
        model = Document
        fields = ('name', 'document', 'document_type', 'comments', 'tags')


class DocumentFilterForm(NetBoxModelFilterSetForm):
    model = Document

    name = CharField(
        required=False
    )

    document_type_id = DynamicModelMultipleChoiceField(
        queryset=DocumentType.objects.all(),
        required=False,
    )

    tag = TagFilterField(model)


# Document Type Form & Filter Form
class DocumentTypeForm(NetBoxModelForm):
    class Meta:
        model = DocumentType
        fields = ('name', 'color')


class DocumentTypeFilterForm(NetBoxModelFilterSetForm):
    model = DocumentType

    name = CharField(
        required=False
    )

    slug = CharField(
        required=False
    )


class DocumentLinkForm(NetBoxModelForm):
    document = DynamicModelChoiceField(
        queryset=Document.objects.all(),
        required=True,
        label='Document',
        help_text='Select the document to link to this object.'
    )
    content_type = ContentTypeChoiceField(
        queryset=ContentType.objects.all(),
        limit_choices_to=FeatureQuery('webhooks'),
        required=False,
        help_text="Type of the related object"
    )

    class Meta:
        model = DocumentLink
        fields = ('document', 'content_type', 'object_id')


class DocumentCreateForm(DocumentForm):
    content_type = ContentTypeChoiceField(
        queryset=ContentType.objects.all(),
        limit_choices_to=FeatureQuery('webhooks'),
        required=True,
        help_text="Type of the related object"
    )
    object_id = IntegerField(
        required=True,
        help_text="ID of the related object"
    )

    def save(self, *args, **kwargs):
        document = super().save(*args, **kwargs)
        DocumentLink.objects.create(
            document=document,
            content_type=self.cleaned_data['content_type'],
            object_id=self.cleaned_data['object_id']
        )
        return document
