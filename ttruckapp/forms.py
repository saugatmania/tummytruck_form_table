from django import forms
from django.db.models import fields
from ttruckapp import models
from ttruckapp.models import Package_orders, Customers


class Package_ordersForm(forms.ModelForm):
    class Meta:
        model = Package_orders
        fields = "__all__"


class CustomersForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = "__all__"
