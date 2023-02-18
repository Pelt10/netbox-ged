from django.urls import path
from . import models, views
from netbox.views.generic import ObjectChangeLogView

urlpatterns = (

    path('documents/', views.DocumentListView.as_view(), name='document_list'),
    path('documents/add/', views.DocumentEditView.as_view(), name='document_add'),
    path('documents/addlink/', views.DocumentCreateView.as_view(), name='document_add_link'),
    path('documents/<int:pk>/', views.DocumentView.as_view(), name='document'),
    path('documents/<int:pk>/edit/', views.DocumentEditView.as_view(), name='document_edit'),
    path('documents/<int:pk>/delete/', views.DocumentDeleteView.as_view(), name='document_delete'),
    path('documents/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='document_changelog', kwargs={
        'model': models.Document
    }),

    path('types/', views.DocumentTypeListView.as_view(), name='documenttype_list'),
    path('types/add/', views.DocumentTypeEditView.as_view(), name='documenttype_add'),
    path('types/<int:pk>/', views.DocumentTypeView.as_view(), name='documenttype'),
    path('types/<int:pk>/edit/', views.DocumentTypeEditView.as_view(), name='documenttype_edit'),
    path('types/<int:pk>/delete/', views.DocumentTypeDeleteView.as_view(), name='documenttype_delete'),
    path('types/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='documenttype_changelog', kwargs={
        'model': models.DocumentType
    }),

    path('link/add/', views.DocumentLinkEditView.as_view(), name='documentlink_add'),
    path('link/<int:pk>/delete', views.DocumentLinkDeleteView.as_view(), name='documentlink_delete'),

)
