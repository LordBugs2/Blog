from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from .serializers import PostSerializer, CategorySerializer
from .models import Post, Category
from rest_framework.response import Response

# Create your views here.


class PostView(generics.ListAPIView):
    queryset = Post.objects.filter()
    serializer_class = PostSerializer


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.filter()
    serializer_class = CategorySerializer


class get_post_by_category(APIView):
    serializer_class = PostSerializer
    lookup_url_kwarg = 'category'

    def get(self, request, format=None):
        category = request.GET.get(self.lookup_url_kwarg)
        posts = Post.objects.filter(category=category)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class get_categoryid_by_name(APIView):
    serializer_class = PostSerializer
    lookup_url_kwarg = 'category'

    def get(self, request, format=None):
        category = request.GET.get(self.lookup_url_kwarg)
        categories = Category.objects.filter(category=category)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)