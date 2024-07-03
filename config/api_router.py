from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from book_system.users.api.views import UserViewSet
from book_system.api.views import AuthorViewSet, GenreViewSet, BookViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("author", AuthorViewSet)
router.register("genre", GenreViewSet)
router.register("book", BookViewSet)


app_name = "api"
urlpatterns = router.urls
