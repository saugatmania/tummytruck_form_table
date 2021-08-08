from django.db import models
from django.db.models.base import Model
from django.db.models.fields import related

# Create your models here.
DELIVER_CHOICES = (
    ("pending", "PENDING"),
    ("delivered", "DELIVERED"),
    ("return", "RETURN")
)
PACKAGE_CHOICES = (
    ("employee_package", "EMPLOYEE PACKAGE"),
    ("total_veg_package", "TOTAL VEG PACKAGE")
)
WEEK = (
    ("first_week", "FIRST WEEK"),
    ("second_week", "SECOND WEEK"),
    ("third_week", "THIRD WEEK"),
    ("fourth_week", "FOURTH WEEK")
)
DAY = (
    ("sunday", "SUNDAY"),
    ("monday", "MONDAY"),
    ("tuesday", "TUESDAY"),
    ("wednesday", "WEDNESDAY"),
    ("thursday", "THURSDAY"),
    ("friday", "FRIDAY"),
    ("saturday", "SATURDAY")
)
PARENT = (
    ("dairy", "DAIRY"),
    ("beverages", "BEVERAGES"),
    ("hard drinks", "HARD DRINKS"),
    ("soft drinks", "SOFT DRINKS"),
    ("groceries", "GROCERIES"),
    ("kitchen item", "KITCHEN ITEM"),
    ("madi in nepal", "MADE IN NEPAL"),
    ("restaurants", "RESTAURANTS")
)


class Customers(models.Model):
    customer = models.CharField(max_length=100)
    phone = models.IntegerField()

    def __str__(self):
        return self.customer


class Package_orders(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=100)
    ordered = models.BooleanField()
    delivered = models.CharField(max_length=50, choices=DELIVER_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    remarks = models.TextField()


class Package_product_purchases(models.Model):
    package = models.CharField(max_length=50, choices=PACKAGE_CHOICES)
    week = models.CharField(max_length=50, choices=WEEK)
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=5, decimal_places=2)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    checkout = models.BooleanField()


class Product_orders(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=100)
    ordered = models.BooleanField()
    delivered = models.CharField(max_length=50, choices=DELIVER_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    remarks = models.TextField()


class Product_purchases(models.Model):
    product = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)
    ordered = models.BooleanField()
    total_price = models.DecimalField(max_digits=5, decimal_places=2)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    checkout = models.BooleanField()


class Package_products(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    package = models.CharField(max_length=50, choices=PACKAGE_CHOICES)
    week = models.CharField(max_length=50, choices=WEEK)
    day = models.CharField(max_length=50, choices=DAY)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Packages(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Product_categorys(models.Model):
    name = models.CharField(max_length=100)
    parent = models.CharField(max_length=50, choices=PARENT)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Product_package_price_historys(models.Model):
    package_product = models.CharField(max_length=100)
    old_price = models.DecimalField(max_digits=5, decimal_places=2)
    current_price = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Blog_posts(models.Model):
    description = models.TextField()
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)


class Email_otps(models.Model):
    phone = models.ForeignKey(Customers, on_delete=models.CASCADE)
    otp = models.IntegerField()
    validated = models.BooleanField()
    count = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    forgot = models.BooleanField()
    forgot_logged = models.BooleanField()


class Profiles(models.Model):
    user = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone = models.ForeignKey(Customers, on_delete=models.CASCADE)
    lunch_time = models.IntegerField()


class User_notifications(models.Model):
    user = models.CharField(max_length=100)
    phone = models.ForeignKey(Customers, on_delete=models.CASCADE)
    message = models.TextField()
    title = models.CharField(max_length=50)


class Users(models.Model):
    email = models.EmailField(max_length=100)
    phone = models.ForeignKey(Customers, on_delete=models.CASCADE)
    password = models.CharField(max_length=100)
    password_confirmation = models.CharField(max_length=100)
