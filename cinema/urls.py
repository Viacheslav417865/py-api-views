from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GenreList, GenreDetail,
    ActorList, ActorDetail,
    CinemaHallViewSet,
    MovieViewSet
)

router = DefaultRouter()
router.register(r"movies", MovieViewSet)

urlpatterns = [
    path("api/cinema/genres/",
         GenreList.as_view(),
         name="genre-list"),
    path("api/cinema/genres/<int:pk>/",
         GenreDetail.as_view(),
         name="genre-detail"),
    path("api/cinema/actors/",
         ActorList.as_view(),
         name="actor-list"),
    path("api/cinema/actors/<int:pk>/",
         ActorDetail.as_view(),
         name="actor-detail"),
    path("api/cinema/cinema_halls/",
         CinemaHallViewSet.as_view({"get": "list", "post": "create"})),
    path("api/cinema/cinema_halls/<int:pk>/",
         CinemaHallViewSet.as_view({"get": "retrieve",
                                    "put": "update",
                                    "patch": "partial_update",
                                    "delete": "destroy"})),
    path("", include(router.urls)),
]
