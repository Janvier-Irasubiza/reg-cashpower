from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('users/', views.GetAllUsers.as_view(), name='users'),
    path('user/<int:id>/', views.GetUser.as_view(), name='user'),
    path('change-password/', views.ChangePassword.as_view(), name="change_password"),
    path('requests/', views.RequestsView.as_view(), name="requests"),
    path('new-requests/', views.NewRequestsView.as_view(), name="requests"),
    path('replace-requests/', views.ReplaceRequestsView.as_view(), name="new-requests"),
    path('repair-requests/', views.RepairRequestsView.as_view(), name="repair-requests"),
    path('displace-requests/', views.DisplaceRequestsView.as_view(), name="diaplce-requests"),
    path('user-requests/<int:user>/', views.UserRequestsView.as_view(), name="user_requests"),
    path('request/<int:req>', views.RequestView.as_view(), name="request"),
    path('update-request/<int:req>', views.UpdateRequest.as_view(), name="request"),
    path('uploads/', views.UploadsView.as_view(), name="uploads"),
    path('req-uploads/<int:req>/', views.UploadsByRequestView.as_view(), name='uploads_by_request'),
    path('dispenses/', views.Dispenses.as_view(), name="dispenses"),
    path('user-dispenses/<int:user>/', views.UserDispenses.as_view(), name="user_dispenses"),
    re_path('login', views.login_view),
    re_path('admin-login', views.admin_login),
    re_path('logout', views.logout_view),
    path('test-token/', views.test_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
