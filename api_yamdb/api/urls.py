from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    GenreViewSet,
    CategoryViewSet,
    TitleViewSet,
    ReviewViewSet,
    CommentViewSet,
    UserViewSet,
    RegistrationView,
    GetJWTokenView,
)

app_name = 'api'

router_v1 = DefaultRouter()

router_v1.register(
    r'genres',
    GenreViewSet,
    basename='genres'
)
router_v1.register(
    r'categories',
    CategoryViewSet,
    basename='categories'
)
router_v1.register(
    r'titles',
    TitleViewSet,
    basename='titles'
)

router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

router_v1.register(
    r'users',
    UserViewSet,
    basename='users',
)

urlpatterns = [
    path('v1/auth/signup/', RegistrationView.as_view()),
    path('v1/auth/token/', GetJWTokenView.as_view()),
    path('v1/', include(router_v1.urls)),
]
