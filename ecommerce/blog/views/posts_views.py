from django.views import generic
from django.db.models import Q
from blog.models.posts import Post, PostCategory
from blog.forms.comment_form import CommentForm
from blog.views.comment_view import CommentFormView


class CategoryListView(generic.ListView):
    model = PostCategory
    # cesta k templatu ze složky templates (je možné sdílet mezi aplikacemi)
    template_name = "blog/post_categories_list.html"
    # pod tímto jménem budeme volat list objektů v templatu
    context_object_name = "categories"

    paginate_by = 10


class PostCategoryDetailView(generic.DetailView):
    model = PostCategory
    template_name = "blog/post_category_detail.html"
    context_object_name = "posts"


class PostIndex(generic.ListView):
    model = Post
    # cesta k templatu ze složky templates (je možné sdílet mezi aplikacemi)
    template_name = "blog/home.html"
    # pod tímto jménem budeme volat list objektů v templatu
    context_object_name = "posts"

    paginate_by = 10

    def get_queryset(self):
        statuses = Post.objects.filter(Q(status=1) | Q(status=2)).order_by(
            "-created_on"
        )
        return statuses


class CurrentPostView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["comments"] = self.object.comments.filter(active=True)
        context["form"] = CommentForm()

        comment_form_view = CommentFormView()
        response = comment_form_view.get(self.request)
        if response.status_code == 302:
            context["url_action"] = response.url
        else:
            context["url_action"] = "comment/"
        return context

    def post(self, request, *args, **kwargs):
        return CommentFormView.as_view()(request, *args, **kwargs)
