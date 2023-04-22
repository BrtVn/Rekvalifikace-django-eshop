from django.forms import ModelForm
from blog.models.comments import Post
from users.models.users import CustomUser


from blog.models.posts import PostCategory


class PostCategoryForm(ModelForm):
    class Meta:
        model = PostCategory
        fields = "__all__"


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = CustomUser.objects.filter(
            is_admin=True)
