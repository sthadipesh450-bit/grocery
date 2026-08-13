from django.urls import path

from .views import RoleDetailAPIView, RoleListCreateAPIView, UserDetailAPIView, UserListCreateAPIView

urlpatterns = [
    path("", UserListCreateAPIView.as_view(), name="user-list-create"),
    path("<int:pk>/", UserDetailAPIView.as_view(), name="user-detail"),
    path("roles/", RoleListCreateAPIView.as_view(), name="role-list-create"),
    path("roles/<int:pk>/", RoleDetailAPIView.as_view(), name="role-detail"),
]
