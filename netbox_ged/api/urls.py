from netbox.api.routers import NetBoxRouter

from netbox_ged.api.views import DocumentViewSet, DocumentTypeViewSet

app_name = 'netbox_ged'

router = NetBoxRouter()
router.register('documents', DocumentViewSet)
router.register('documenttype', DocumentTypeViewSet)

urlpatterns = router.urls