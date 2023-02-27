from django.urls import path
from . import views, url_handlers


urlpatterns = [
    path("index/", url_handlers.index_handler),
    path("", views.ProductsIndex.as_view(), name="index"),
    path("category-list/", views.CategoryTreeIndex.as_view(), name="category_list"),
    path(
        "category-detail/<int:pk>/",
        views.CurrentProductCategoryView.as_view(),
        name="category_detail",
    ),
    path(
        "product-detail/<int:pk>/",
        views.CurrentProductView.as_view(),
        name="product_detail",
    ),
    path("contact/", views.ContactFormView.as_view(), name="contact_form"),
    path("cart/", views.CartView.as_view(), name="cart"),
    # admin
    path("products/", views.ProductListView.as_view(), name="list_products"),
    path("create/", views.ProductCreateView.as_view(), name="create_product"),
    path("update/<int:pk>/", views.ProductUpdateView.as_view(), name="update_product"),
    # path('delete-image/<int:pk>/', views.delete_image, name='delete_image'),
    # path('delete-variant/<int:pk>/', views.delete_variant, name='delete_variant'),
]
