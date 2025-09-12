from django.urls import path
from .views import HelloView, CachorroListView , CreateCachorro , CachorroUpdate , CachorroDelete

urlpatterns = [
    path('', HelloView.as_view(), name='index'),
    path('listar/', CachorroListView.as_view(), name='listar_cachorros'),
    path('create/',CreateCachorro.as_view(), name='url_create'),
    path('update/<int:pk>',CachorroUpdate.as_view(), name='url_update'),
    path('delete/<int:pk>',CachorroDelete.as_view(),name = 'url_delete'),
    ]