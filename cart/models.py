from django.db import models


# Create your models here.
class Order(models.Model):
    userName = models.CharField(max_length=150, db_index=True)
    address = models.CharField(max_length=150, default="didn't set")
    order = models.CharField(max_length=30000)

    class Meta:
        ordering = ('userName',)
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    def __str__(self):
        return self.userName
