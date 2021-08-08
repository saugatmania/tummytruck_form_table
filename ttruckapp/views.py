from ttruckapp.models import Blog_posts, Email_otps, Package_orders, Package_product_purchases, Product_categorys, Product_orders, Product_package_price_historys, Product_purchases, Package_products, Products, Packages, Profiles, User_notifications, Users
from django.shortcuts import render, reverse
from ttruckapp.forms import Package_ordersForm, CustomersForm
from django.http.response import HttpResponseRedirect


def home(request):
    form = CustomersForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("ttruckapp:purchase"))
    return render(request, 'home.html', {'form': form})


def purchase_form(request):
    form = Package_ordersForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("ttruckapp:purchase"))
    return render(request, 'purchase_form.html', {'form': form})


# def purchase(request):
    # package_orders = Package_orders.objects.all()
    # package_product_purchases = Package_product_purchases.objects.all()
    # product_orders = Product_orders.objects.all()
    # product_purchases = Product_purchases.objects.all()

    # context = {"package_orders": package_orders, 'package_product_purchases': package_product_purchases,
    #            'product_order': product_orders, 'product_purchases': product_purchases}

    # return render(request, 'purchase.html', context)


def package_orders(request):
    package_orders = Package_orders.objects.all()

    context = {'package_orders': package_orders}
    return render(request, 'package_orders.html', context)


def package_product_purchases(request):
    package_product_purchases = Package_product_purchases.objects.all()

    context = {'package_product_purchases': package_product_purchases}
    return render(request, 'package_product_purchases.html', context)


def product_orders(request):
    product_orders = Product_orders.objects.all()

    context = {'product_order': product_orders}
    return render(request, 'product_orders.html', context)


def product_purchases(request):
    product_purchases = Product_purchases.objects.all()

    context = {'product_purchases': product_purchases}
    return render(request, 'product_purchases.html', context)


# def services(request):
    # package_products = Package_products.objects.all()
    # packages = Packages.objects.all()
    # product_categorys = Product_categorys.objects.all()
    # product_package_price_historys = Product_package_price_historys.objects.all()
    # products = Products.objects.all()

    # context = {'package_products': package_products, 'packages': packages, 'product_categorys': product_categorys,
    #            'product_package_price_historys': product_package_price_historys, 'products': products}
    # return render(request, 'service.html', context)


def package_products(request):
    package_products = Package_products.objects.all()

    context = {'package_products': package_products}
    return render(request, 'package_products.html', context)


def packages(request):
    packages = Packages.objects.all()

    context = {'packages': packages}
    return render(request, 'packages.html', context)


def product_categorys(request):
    product_categorys = Product_categorys.objects.all()

    context = {'product_categorys': product_categorys}
    return render(request, 'product_categorys.html', context)


def product_package_price_historys(request):
    product_package_price_historys = Product_package_price_historys.objects.all()

    context = {'product_package_price_historys': product_package_price_historys}
    return render(request, 'product_package_price_historys.html', context)


def products(request):
    products = Products.objects.all()

    context = {'products': products}
    return render(request, 'products.html', context)


# def useraccount(request):
#     blog_posts = Blog_posts.objects.all()
#     email_otps = Email_otps.objects.all()
#     profiles = Profiles.objects.all()
#     user_notifications = User_notifications.objects.all()
#     users = Users.objects.all()

#     context = {'blog_posts': blog_posts, 'email_otps': email_otps,
#                'profiles': profiles, 'user_notifications': user_notifications, 'users': users}
#     return render(request, 'useraccount.html', context)


def blog_posts(request):
    blog_posts = Blog_posts.objects.all()

    context = {'blog_posts': blog_posts}
    return render(request, 'blog_posts.html', context)


def email_otps(request):
    email_otps = Email_otps.objects.all()

    context = {'email_otps': email_otps}
    return render(request, 'email_otps.html', context)


def profiles(request):
    profiles = Profiles.objects.all()

    context = {'profiles': profiles}
    return render(request, 'profiles.html', context)


def user_notifications(request):
    user_notifications = User_notifications.objects.all()

    context = {'user_notifications': user_notifications}
    return render(request, 'user_notifications.html', context)


def users(request):
    users = Users.objects.all()

    context = {'users': users}
    return render(request, 'users.html', context)
