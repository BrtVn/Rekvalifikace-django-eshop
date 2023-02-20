from . import views, url_handlers
from django.urls import path, include

urlpatterns = [
    path('index/', url_handlers.index_handler),
    path('', views.ProductsIndex.as_view(), name="index"),
    path('category-list/',
         views.CategoryTreeIndex.as_view(), name="category_list"),
    path('category-detail/<int:pk>/',
         views.CurrentProductCategoryView.as_view(), name="category_detail"),
    path('product-detail/<int:pk>/',
         views.CurrentProductView.as_view(), name="product_detail"),
    path('contact/',
         views.ContactFormView.as_view(), name="contact_form"),
    path("register/", views.UserViewRegister.as_view(), name="register"),
    path("login/", views.UserViewLogin.as_view(), name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("profile/", views.ProfileFormView.as_view(), name="profile"),
    # path('place-order/<int:i>/', views.PlaceOrderView.as_view(), name='place_order'),
    # path('product-detail/<int:pk>/add-item/', views.add_to_cart, name='place_order'),
    path('cart/', views.CartView.as_view(), name='cart'),
]
