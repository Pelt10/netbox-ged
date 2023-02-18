from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from netbox.models import NetBoxModel
from utilities.fields import ColorField

from .utils import file_upload


class DocumentType(NetBoxModel):
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text='Name of the document type'
    )

    color = ColorField()

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Document Types"
        verbose_name = "Document Type"

    def __str__(self):
        return self.name

    # Needed for linkify in tables
    def get_absolute_url(self):
        return reverse('plugins:netbox_ged:documenttype', args=[self.pk])


class Document(NetBoxModel):
    name = models.CharField(
        max_length=100,
        blank=True,
        help_text='(Optional) Specify a name to display for this document. If no name is specified, the filename or url will be used.'
    )

    document = models.FileField(
        upload_to=file_upload,
        blank=True
    )

    document_type = models.ForeignKey(
        to=DocumentType,
        on_delete=models.PROTECT,
        related_name='documents',
    )

    comments = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ('-created', 'name')
        verbose_name_plural = "Documents"
        verbose_name = "Document"

    def get_document_type_color(self):
        return self.document_type.color

    @property
    def size(self):
        """
        Wrapper around `document.size` to suppress an OSError in case the file is inaccessible.     Also opportunistically
        catch other exceptions that we know other storage back-ends to throw.
        """
        expected_exceptions = [OSError]

        try:
            from botocore.exceptions import ClientError
            expected_exceptions.append(ClientError)
        except ImportError:
            pass

        try:
            return self.document.size
        except:
            return None

    @property
    def filename(self):
        filename = self.document.name.rsplit('/', 1)[-1]
        return filename.split('_', 1)[1]

    def __str__(self):
        if self.name:
            return self.name

        elif self.document:
            filename = self.document.name.rsplit('/', 1)[-1]
            return filename.split('_', 1)[1]

        else:
            return ""

    def get_absolute_url(self):
        return reverse('plugins:netbox_ged:document', args=[self.pk])

    def clean(self):
        super().clean()

        # Must have an uploaded document
        if not self.document:
            raise ValidationError("A document must contain an uploaded file")

    def delete(self, *args, **kwargs):
        _name = self.document.name

        # Delete file from disk
        super().delete(*args, **kwargs)
        self.document.delete(save=False)

        # Restore the name of the document as it's re-used in the notifications later
        self.document.name = _name


class DocumentLink(NetBoxModel):
    document = models.ForeignKey(
        to=Document,
        on_delete=models.PROTECT,
        related_name='relative_objects',
    )
    content_type = models.ForeignKey(
        to=ContentType,
        on_delete=models.PROTECT,
        related_name='documents',
    )
    object_id = models.PositiveIntegerField()
    object_content = GenericForeignKey(
        ct_field='content_type',
        fk_field='object_id'
    )
