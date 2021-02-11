from django.urls import path
from .views import PostView, CategoryView, get_post_by_category

urlpatterns = [
    path('posts', PostView.as_view()),
    path('categories', CategoryView.as_view()),
    path('get-post-by-category', get_post_by_category.as_view())
]
