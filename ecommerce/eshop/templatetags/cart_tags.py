from django import template
from eshop.models.orders import Cart

register = template.Library()


def get_cart(context):
    request = context['request']
    status = "DRAFT"
    cart_id = request.session.get('cart_id', {})
    if cart_id:
        try:
            return Cart.objects.get(pk=cart_id, status=status)
        except Cart.DoesNotExist:
            print(
                f"Cart instance with id {cart_id} and status {status} does not exist.")
    return None


@register.simple_tag(takes_context=True)
def get_cart_items(context):
    """ Return all items in cart or None
    Usage:
    {% load cart_tags %}
    {% get_cart_items as cart %}
    {% if cart %} 
    <ul >          
        {% for item in cart.items.all %}
            <li > {{item}} < /li >
        {% endfor %}
    </ul >

    Args:
        context (_type_): _description_

    Returns:
        _type_: _description_
    """

    cart = get_cart(context)
    if cart:
        return cart
    return None


@register.simple_tag(takes_context=True)
def cart_item_count(context):
    # request = context['request']
    # cart_id = request.session.get('cart_id', {})
    # if cart_id:
    #     try:
    #         # cart = get_object_or_404(Cart, pk=cart_id)
    #         cart = Cart.objects.get(pk=cart_id)
    #         return cart.items.all().count()
    #     except Cart.DoesNotExist:
    #         print(f"Cart instance with id {cart_id} does not exist.")
    #         return 0
    # return 0

    cart = get_cart(context)
    if cart:
        return cart.items.all().count()
    return 0
