from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:category_id>', views.product, name='product'),
    path('update_cart/<int:product_id>/<str:action>/', views.update_cart_quantity, name='update_cart'),
    path('product_detail/<int:product_id>', views.product_detail, name='product_detail'),
    
    path('cart/<int:product_id>', views.cart, name='cart'),
    path('cart_view', views.cart_view, name='cart_view'),
    path('clear_cart', views.clear_cart, name='clear_cart'),
    path('remove_from_cart/<int:product_id>', views.remove_from_cart, name='remove_from_cart'),
    path('signup', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    # path('logout', views.logout, name='logout'),
]
urlpatterns += static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)