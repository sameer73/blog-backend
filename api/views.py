""" Create your views here."""
from rest_framework import viewsets, permissions
from django.http import Http404
from django.db.models import Count
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post,Category,Comment
from .serializers import PostSerializer,CategorySerializer,PostAllSerializer,CommentSerializer,CommentAllSerializer

class PostViewSet(viewsets.ModelViewSet):
    """post viewset"""
    queryset = Post.objects.all().order_by('-created_at')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        # based on action use different serializer
        if self.action == 'retrieve' or self.action == 'update' or self.action=='create':
            return PostSerializer
        # For list view or other actions, use GET serializer
        return PostAllSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = queryset.annotate(comment_count=Count('post_comments'))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = PostAllSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
    def get_queryset(self,*args, **kwargs):
        queryset = self.queryset.prefetch_related('category').select_related('author')
        return queryset.order_by('-id')
    
class CategoryViewSet(viewsets.ModelViewSet):
    """category viewset"""
    queryset = Category.objects.all().order_by('-created_at')
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

class CommentViewSet(viewsets.ModelViewSet):
    """category viewset"""   
    queryset = Comment.objects.all().order_by('-created_at')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        print(self.action,'---')
        # If a specific post (detail view) is requested, use specific serializer
        if self.action == 'update' or self.action=='create':
            return CommentSerializer
        # For list view or other actions, use GET serializer
        return CommentAllSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    def get_queryset(self,*args, **kwargs):
        return self.queryset.order_by('-id')
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        post_id = request.query_params.get('post_id', None)
        if post_id:
            queryset = queryset.filter(post_id=post_id).order_by('-id')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = CommentAllSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

class GetPostDetail(APIView):
    """get by url"""
    
    def get_object(self, url):
        """get object by url"""
        try:
            return Post.objects.get(blog_url=url)
        except Post.DoesNotExist:
            raise Http404
   
    def get(self, request, url, format=None):
        snippet = self.get_object(url)
        serializer = PostAllSerializer(snippet)
        return Response(serializer.data)

