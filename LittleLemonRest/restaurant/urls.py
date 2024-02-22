from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='single_menu'),
    path('booking/', include(router.urls),name='booking'),
    path('message/', views.msg),
]
