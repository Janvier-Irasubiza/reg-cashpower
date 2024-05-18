from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('users/', views.GetAllUsers.as_view(), name='users'),
    path('user/<int:id>/', views.GetUser.as_view(), name='user'),
    path('requests/', views.RequestsView.as_view(), name="requests"),
    path('request/<int:req>', views.RequestView.as_view(), name="request"),
    path('uploads/', views.UploadsView.as_view(), name="request"),
    path('req-uploads/<int:req>/', views.UploadsByRequestView.as_view(), name='uploads_by_request'),
    # path('clients/', views.ClientsView.as_view(), name='clients'),
    # path('client/<int:client>/', views.ClientView.as_view(), name='client'),
    re_path('login', views.login_view),
    re_path('logout', views.logout_view),
    path('test-token/', views.test_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
