from django.contrib.contenttypes.models import ContentType

from extras.plugins import PluginTemplateExtension
from extras.utils import FeatureQuery

from netbox_ged.models import Document


class DocumentTemplateExtension(PluginTemplateExtension):

    def left_page(self):
        content_type = ContentType.objects.get(
            app_label=self.context['object']._meta.app_label,
            model=self.context['object']._meta.model_name
        )

        documents = Document.objects.filter(
                relative_objects__content_type=content_type.id,
                relative_objects__object_id=self.context['object'].pk
        )

        for document in documents:
            document.link = document.relative_objects.get(
                content_type=content_type.id,
                object_id=self.context['object'].pk,
                document=document
            ).id

        return self.render('netbox_ged/document_include.html', extra_context={
            'documents': documents,
            'content_type': content_type,
        })


template_extensions = []
for ct in ContentType.objects.filter(FeatureQuery('webhooks').get_query()):
    class_name = ct.model_class().__name__ + 'DocumentList'
    model_name = "%s.%s" % (ct.app_label, ct.model)
    template_extensions.append(type(class_name, (DocumentTemplateExtension,), {'model': model_name}))

