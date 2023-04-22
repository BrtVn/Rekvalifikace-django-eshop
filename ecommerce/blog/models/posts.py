from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit


# class PostQuerySet(models.QuerySet):
#     def search(self, **kwargs):
#         qs = self
#         if kwargs.get('q', ''):
#             qs = qs.filter(title__icontains=kwargs['q'])
#         if kwargs.get('government_type', []):
#             qs = qs.filter(government_type=kwargs['government_type'])
#         if kwargs.get('industry', []):
#             qs = qs.filter(industry=kwargs['industry'])
#         return qs


STATUS = (
    (0, "Draft"),
    (1, "Published"),
    (2, "Promoted"),
    (3, "Useful links")
)

# definovat jako enum?


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=False)
    author = models.ForeignKey(
        "users.CustomUser", on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    post_image = models.ImageField(upload_to="blog/uploads/posts")
    post_category = models.ForeignKey(
        "PostCategory", on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='blog_post_categories'
    )

    image_thumbnail_promoted = ImageSpecField(source='post_image',
                                              processors=[
                                                  ResizeToFit(850, 350)],
                                              format='JPEG',
                                              options={'quality': 100})
    image_thumbnail = ImageSpecField(source='post_image',
                                     processors=[
                                         ResizeToFit(700, 350)],
                                     format='JPEG',
                                     options={'quality': 100})
    image_detail = ImageSpecField(source='post_image',
                                  processors=[ResizeToFit(850, 350)],
                                  format='JPEG',
                                  options={'quality': 100})
    search_thumbnail = ImageSpecField(source='post_image',
                                      processors=[
                                          ResizeToFit(240, 120)],
                                      format='JPEG',
                                      options={'quality': 100})

    # objects = PostQuerySet.as_manager()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})  # new


class PostCategory(models.Model):
    slug = models.SlugField(max_length=200, unique=True, null=False)
    category_name = models.CharField(max_length=50)
    # category_parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name="children" )
    category_description = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Kategorie příspěvku"
        verbose_name_plural = "Kategorie příspěvků"

    def __str__(self) -> str:
        return f"{self.category_name}"

    @staticmethod
    def return_all_categories():
        return PostCategory.objects.all()

    @staticmethod
    def return_category_description(description):
        return PostCategory.objects.filter(category_description=description)

    def get_absolute_url(self):
        if self.slug:
            return reverse("post_category_detail", kwargs={"slug": self.slug})
        return "/"
