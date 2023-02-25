from django.db import models
from shop_app.models import Product1
# Create your models here.
class Cart1(models.Model):
    cart_id=models.CharField(max_length=250,blank=True)
    date_added=models.DateField(auto_now_add=True)

    class Meta:
        db_table='Cart1'
        ordering=['date_added']

    def __str__(self):
        return '{}'.format(self.cart_id)
class CartItem1(models.Model):
    product=models.ForeignKey(Product1,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart1,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)

    class Meta:
        db_table='CartItem1'

    def sub_total(self):
        return self.product.price *self.quantity
    def __str__(self):
        return '{}'.format(self.product)
