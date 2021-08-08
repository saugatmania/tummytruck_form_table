from django.urls import path
from ttruckapp import views


app_name = 'ttruckapp'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('form/', views.purchase_form, name='form'),
    path('package_orders/', views.package_orders, name='package_orders'),
    path('package_product_purchases/', views.package_product_purchases,
         name='package_product_purchases'),
    path('product_orders/', views.product_orders, name='product_orders'),
    path('product_purchases/', views.product_purchases, name='product_purchases'),

    path('package_products/', views.package_products, name='package_products'),
    path('packages/', views.packages, name='packages'),
    path('product_categorys/', views.product_categorys, name='product_categorys'),
    path('product_package_price_historys/', views.product_package_price_historys,
         name='product_package_price_historys'),
    path('products/', views.products, name='products'),

    path('blog_posts/', views.blog_posts, name='blog_posts'),
    path('email_otps/', views.email_otps, name='email_otps'),
    path('profiles/', views.profiles, name='profiles'),
    path('user_notifications/', views.user_notifications,
         name='user_notifications'),
    path('users/', views.users, name='users'),

]
