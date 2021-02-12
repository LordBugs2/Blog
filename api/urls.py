from django.urls import path
from .views import PostView, CategoryView, get_post_by_category, get_categoryid_by_name

urlpatterns = [
    path('posts', PostView.as_view()),
    path('categories', CategoryView.as_view()),
    path('get-post-by-category', get_post_by_category.as_view()),
    path('get-categoryid-by-name', get_categoryid_by_name.as_view())
]
