from django import template
from blog.models.posts import PostCategory
register = template.Library()


@register.simple_tag()
def get_post_categories():
    """ Return all items in cart or None
    Usage:
    {% load tags %}
    {% get_post_categories as categories %}
    {% if cart %} 
    <ul >          
        {% for item in categories %}
            <li > {{item}} < /li >
        {% endfor %}
    </ul >

    Args:


    Returns:
        _type_: _description_
    """

    categories = PostCategory.objects.all()
    if categories:
        return categories
    return None
