from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='login/', permanent=False)),
    path('new-request/', views.new_request, name='new-request'),
    path('all-open-requests/', views.all_open_requests, name='all-open-requests'),
    path('open-request-detail/<int:request_id>/', views.open_request_detail, name='open-request-detail'),
    path('closed-requests/', views.closed_requests, name='closed-requests'),
]
