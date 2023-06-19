from django.contrib import admin
from django.urls import path
from .views import snack_listView,snack_detailView, snack_createView,snack_updateView,snack_deleteView

urlpatterns = [
    path('',snack_listView.as_view(), name='snack_list'),
    path('<int:pk>/',snack_detailView.as_view(), name='snack_detail'),
    path('create/',snack_createView.as_view(), name="snack_create"),
    path('update/<int:pk>',snack_updateView.as_view(), name="snack_update"),
    path('delete/<int:pk>',snack_deleteView.as_view(), name="snack_delete"),
]