from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib import messages
from blog.models.posts import Post
from blog.models.comments import Comment
from blog.forms.comment_form import CommentForm


class CommentFormView(generic.edit.CreateView):
    form_class = CommentForm
    model = Comment
    template_name = "blog/post_detail.html"

    def get(self, request):
        form = self.form_class(None)
        url_action = "comment/"
        context = {"form": form,
                   "url_action": url_action}
        return render(request, self.template_name, context)

    
    def form_valid(self, form):
        form.instance.post = self.get_post()
        messages.info(self.request, 'Your comment is awaiting moderation')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Comment error')
        return super().form_invalid(form)

    def get_post(self):
        return get_object_or_404(Post, slug=self.kwargs['slug'])

    def get_success_url(self):
        #return reverse('post_detail')
        return reverse('post_detail', kwargs={'slug': self.kwargs['slug']})

    def post(self, request, *args, **kwargs):
        self.object = None
        return super().post(request, *args, **kwargs)
