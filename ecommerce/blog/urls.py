from . import views
from django.urls import path

# app_name = 'blog'

urlpatterns = [
    path("categories/", views.CategoryListView.as_view(), name="post_categories"),
    path("categories/<slug:slug>/",
         views.PostCategoryDetailView.as_view(), name="post_category_detail"),

    path("", views.PostIndex.as_view(), name="home"),
    path("<slug:slug>/", views.CurrentPostView.as_view(), name="post_detail"),
    path("<slug:slug>/comment/", views.CurrentPostView.as_view(), name="add_comment"),
]
