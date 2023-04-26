from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models.posts import Post, PostCategory
from moderator.forms.posts_forms import PostForm, PostCategoryForm


class PostCategoryListView(LoginRequiredMixin, ListView):
    model = PostCategory
    template_name = "moderator/post_categories_list.html"
    context_object_name = "categories"


class PostCategoryCreateView(LoginRequiredMixin, CreateView):
    model = PostCategory
    form_class = PostCategoryForm
    success_url = reverse_lazy("list_post_categories")
    template_name = "moderator/post_category_create_or_update.html"


class PostCategoryUpdateView(
    LoginRequiredMixin, UpdateView
):  # pylint: disable=too-many-ancestors

    model = PostCategory
    form_class = PostCategoryForm
    success_url = reverse_lazy("list_post_categories")
    template_name = "moderator/post_category_create_or_update.html"


class PostCategoryDeleteView(
    LoginRequiredMixin, DeleteView
):  # pylint: disable=too-many-ancestors
    """Smazání konkrétní kategoorie

    Args:
        LoginRequiredMixin (_type_): _description_
        DeleteView (_type_): _description_
    """

    model = PostCategory
    success_url = reverse_lazy("list_post_categories")


class PostListView(ListView):
    model = Post
    template_name = "moderator/posts_list.html"
    context_object_name = "posts"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("list_posts")
    template_name = "moderator/post_create_or_update.html"


class PostUpdateView(
    LoginRequiredMixin, UpdateView
):  # pylint: disable=too-many-ancestors

    model = Post
    form_class = PostForm
    success_url = reverse_lazy("list_posts")
    template_name = "moderator/post_create_or_update.html"


class PostDeleteView(
    LoginRequiredMixin, DeleteView
):  # pylint: disable=too-many-ancestors
    """Smazání konkrétního postu

    Args:
        LoginRequiredMixin (_type_): _description_
        DeleteView (_type_): _description_
    """

    model = Post
    success_url = reverse_lazy("list_posts")
