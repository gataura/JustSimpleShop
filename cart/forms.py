from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 36)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class OrderForm(forms.Form):
    userName = forms.CharField(max_length=256)
    address = forms.CharField(max_length=256)
