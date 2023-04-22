from django.urls import path
from . import views, url_handlers


urlpatterns = [
    path("index/", url_handlers.index_handler),
    path("", views.ProductsIndex.as_view(), name="index"),
    path("category-list/", views.CategoryTreeIndex.as_view(), name="category_list"),
    path(
        "category-detail/<slug:slug>/",
        views.CurrentProductCategoryView.as_view(),
        name="category_detail",
    ),
    path(
        "product-detail/<slug:slug>/",
        views.CurrentProductView.as_view(),
        name="product_detail",
    ),
    path("contact/", views.ContactFormView.as_view(), name="contact_form"),
    path("cart/", views.CartListView.as_view(), name="cart"),
    path('add-to-cart/',
         views.AddToCartView.as_view(), name='add_to_cart'),
    path('cart/delete/<int:pk>/',
         views.CartDeleteView.as_view(), name='remove_from_cart'),
    path('cart/update/<int:pk>/',
         views.CartUpdateView.as_view(), name='update_item_cart'),
    path('cart/update/payment-method/<int:pk>/',
         views.CartPaymentMethodView.as_view(), name='update_payment_method_cart'),
    path('cart/update/delivery-method/<int:pk>/',
         views.CartDeliveryMethodView.as_view(), name='update_delivery_method_cart'),
    path('order/create/',
         views.CreateOrderView.as_view(), name='create_order'),
    path('order/create/preferred-billing-information/<int:pk>/',
         views.UserPreferredBillingInformationView.as_view(), name='update_preferred_billing_information'),
    path('order/create/preferred-delivery-information/<int:pk>/',
         views.UserPreferredDeliveryInformationView.as_view(), name='update_preferred_delivery_information'),
    path('search/',
         views.SearchFormView.as_view(), name='search'),
    path('search/results/',
         views.SearchResultsTemplateView.as_view(), name='search_results'),
    path('accounts/profile/orders',
         views.OrderProfileListView.as_view(), name='list_orders'),
    path('accounts/profile/orders/<int:pk>',
         views.OrderProfileDetailView.as_view(), name='order_detail'),
    path('tag/<slug:slug>/',
         views.TagDetailView.as_view(), name='tag_detail'),
]
