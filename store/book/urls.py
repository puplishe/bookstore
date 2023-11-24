from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import BookListApiView
router = DefaultRouter()
router.register(r'book', BookListApiView)

urlpatterns = [
    path('', include(router.urls))
]