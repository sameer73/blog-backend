from api.views import PostViewSet,CategoryViewSet,CommentViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path
from api import views
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'category',CategoryViewSet)
router.register(r'comments',CommentViewSet)

urlpatterns = [
    # path('all-blogs/', views.PostList.as_view()),
    path('get-blog/<str:url>/', views.GetPostDetail.as_view()),
]

urlpatterns += router.urls
# urlpatterns += format_suffix_patterns(urlpatterns)