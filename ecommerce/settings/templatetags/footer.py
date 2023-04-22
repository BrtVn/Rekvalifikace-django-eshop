from django import template
from settings.models import GeneralInfo, Contact
from blog.models.posts import Post

register = template.Library()


@register.inclusion_tag("footer.html")
def show_footer():
    general_info = GeneralInfo.objects.first()
    contact = Contact.objects.first()
    articles = Post.objects.filter(status=3)
    return {"general_info": general_info, "contact": contact, "articles": articles, }
