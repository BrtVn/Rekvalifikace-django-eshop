from django.shortcuts import render, redirect
from eshop.models.products import Product
from eshop.models.orders import Order
from django.views.generic import ListView, DetailView, CreateView, View
from django.contrib.auth.decorators import login_required

class CartView(DetailView):

    model = Order
    template_name = 'eshop/cart.html'
    # pod tímto jménem budeme volat list objektů v templatu
    context_object_name = "orders"
    paginate_by = 100  # if pagination is desired

    def get(self, request):
        cart = request.session.get('cart')
        print(cart)
        if cart:
            ids = list(cart.keys())
            products = Product.get_products_by_id(ids)
        else:
            print("No products here")
            products = []
        return render(request, self.template_name, {'products': products})


    def add_to_cart(request, pk):
        product_id =  request.POST.get('product')
        product = Product.objects.get(id=int(product_id))
        cart, created = Order.objects.get_or_create(customer=request.user)
        order_item, created = Product.objects.get_or_create(
            product_name=product, cart=cart)
        if not created:
            order_item.quantity += 1
            order_item.save()
        return redirect('index')




"""
def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        # If the user is authenticated, get their cart
        cart, created = Order.objects.get_or_create(user=request.user)
    else:
        # If the user is not authenticated, get their temporary cart from the session
        cart = request.session.get('cart', {})

    # Add the product to the cart
    product = Product.objects.get(id=product_id)
    cart.products.add(product)

    if request.user.is_authenticated:
        # If the user is authenticated, save the cart to the database
        cart.save()
    else:
        # If the user is not authenticated, save the cart to the session
        request.session['cart'] = cart

    return redirect('view_cart')"""
