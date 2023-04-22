from . import views
from django.urls import path


urlpatterns = [
    path(
        "posts/",
        views.PostListView.as_view(),
        name="list_posts",
    ),
    path(
        "posts/create/",
        views.PostCreateView.as_view(),
        name="create_post",
    ),
    path(
        "posts/update/<int:pk>/",
        views.PostUpdateView.as_view(),
        name="update_post",
    ),
    path(
        "posts/delete/<int:pk>/",
        views.PostDeleteView.as_view(),
        name="delete_post",
    ),
    path(
        "post/categories/",
        views.PostCategoryListView.as_view(),
        name="list_post_categories",
    ),
    path(
        "post/categories/create/",
        views.PostCategoryCreateView.as_view(),
        name="create_post_category",
    ),
    path(
        "post/categories/update/<int:pk>/",
        views.PostCategoryUpdateView.as_view(),
        name="update_post_category",
    ),
    path(
        "post/categories/delete/<int:pk>/",
        views.PostCategoryDeleteView.as_view(),
        name="delete_post_category",
    ),
    path("products/", views.ProductListView.as_view(), name="list_products"),
    path(
        "products/create/",
        views.ProductCreateView.as_view(),
        name="create_product",
    ),
    path(
        "products/update/<int:pk>/",
        views.ProductUpdateView.as_view(),
        name="update_product",
    ),
    path(
        "products/delete/<int:pk>/",
        views.ProductDeleteView.as_view(),
        name="delete_product",
    ),
    path(
        "products/categories/",
        views.ProductCategoryListView.as_view(),
        name="list_product_categories",
    ),
    path(
        "products/categories/create/",
        views.ProductCategoryCreateView.as_view(),
        name="create_product_category",
    ),
    path(
        "products/categories/update/<int:pk>/",
        views.ProductCategoryUpdateView.as_view(),
        name="update_product_category",
    ),
    path(
        "products/categories/delete/<int:pk>/",
        views.ProductCategoryDeleteView.as_view(),
        name="delete_product_category",
    ),
    path(
        "customers/",
        views.CustomersListView.as_view(),
        name="list_customers",
    ),
    path(
        "customers/create/",
        views.CustomerCreateView.as_view(),
        name="create_customer",
    ),
    path(
        "customers/update/<int:pk>/",
        views.CustomerUpdateView.as_view(),
        name="update_customer",
    ),
    path(
        "customers/delete/<int:pk>/",
        views.CustomerDeleteView.as_view(),
        name="delete_customer",
    ),

    path(
        "company-info/",
        views.GeneralInfoListView.as_view(),
        name="list_company_info",
    ),
    path(
        "company-info/create/",
        views.GeneralInfoCreateView.as_view(),
        name="create_company_info",
    ),
    path(
        "company-info/update/<int:pk>/",
        views.GeneralInfoUpdateView.as_view(),
        name="update_company_info",
    ),
    path(
        "company-info/delete/<int:pk>/",
        views.GeneralInfoDeleteView.as_view(),
        name="delete_company_info",
    ),
    path(
        "contact/",
        views.ContactListView.as_view(),
        name="list_contact",
    ),
    path(
        "contact/create/",
        views.ContactCreateView.as_view(),
        name="create_contact",
    ),
    path(
        "contact/update/<int:pk>/",
        views.ContactUpdateView.as_view(),
        name="update_contact",
    ),
    path(
        "contact/delete/<int:pk>/",
        views.ContactDeleteView.as_view(),
        name="delete_contact",
    ),
    path(
        "orders/",
        views.AllOrdersListView.as_view(),
        name="moderator_list_orders",
    ),
    path(
        "orders/update/<int:pk>/",
        views.OrderUpdateView.as_view(),
        name="update_order",
    ),
    path(
        "orders/delete/<int:pk>/",
        views.OrderDeleteView.as_view(),
        name="delete_order",
    ),
    path(
        "orders/cart-items/update/<int:pk>/",
        views.OrderCartItemUpdateview.as_view(),
        name="update_order_cart_item",
    ), path(
        "tags/",
        views.TagsListView.as_view(),
        name="list_tags",
    ),
    path(
        "tags/create/",
        views.TagCreateView.as_view(),
        name="create_tag",
    ),
    path(
        "tags/update/<int:pk>/",
        views.TagUpdateView.as_view(),
        name="update_tag",
    ),
    path(
        "tags/delete/<int:pk>/",
        views.TagDeleteView.as_view(),
        name="delete_tag",
    ),
]