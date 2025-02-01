from rest_framework import serializers
from .models import Post,Category,Comment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model."""
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class PostSerializer(serializers.ModelSerializer):
    """Serializer for Post Model"""
    class Meta:
        model = Post
        fields = ('id','blog_url','category','content','title','status')
        

        
class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category Model"""
    class Meta:
        model = Category
        fields = '__all__'
        
        
class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Category Model"""
    class Meta:
        model = Comment
        fields = ('id','post','content','is_active')

class CommentAllSerializer(serializers.ModelSerializer):
    """Serializer for Category Model"""
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = ['id','post','content','is_active','user','created_at','updated_at']
        read_only_fields = ['__all__']
        
class PostAllSerializer(serializers.ModelSerializer):
    """ataching author category and comments """
    
    comment_count = serializers.IntegerField(read_only=True)
    author = serializers.StringRelatedField(read_only=True)
    category_names = serializers.StringRelatedField(source='category', many=True, read_only=True)
    

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'blog_url', 'content', 'created_at', 
            'updated_at', 'category_names', 'author', 
            'status', 'comment_count'
        ]
        read_only_fields = ['__all__']

# class CommentSerializer(serializers.ModelSerializer):
#     """attaching user and post title"""
#     user = serializers.StringRelatedField(read_only=True)
#     post_title = serializers.StringRelatedField(source='post', read_only=True)

#     class Meta:
#         model = Comment
#         fields = [
#             'id', 'post', 'post_title', 'user', 
#             'content', 'created_at', 'updated_at', 
#             'is_active'
#         ]
#         read_only_fields = ['__all__']
        