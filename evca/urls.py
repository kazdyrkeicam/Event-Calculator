from django.urls import path

from . import views

# app_name = 'evca'

urlpatterns = [
    path('', views.index, name="index"),
    path('add_member/', views.add_member_form, name="add_member"),
    path('member/<int:member_id>/', views.member_detail, name='member_detail'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('add_event/', views.add_event_form, name='add_event'),
]