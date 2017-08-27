from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=99, blank=False, null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=99, blank=False, null=False)
    category = models.ForeignKey(Category)
    volume = models.DecimalField(decimal_places=2, max_digits=9)
    alcohol = models.DecimalField(decimal_places=2, max_digits=9)
    price = models.DecimalField(decimal_places=2, max_digits=9)
    alcohol_price = models.DecimalField(decimal_places=2, max_digits=9)

    class Meta:
        ordering = ['alcohol_price']

    def __str__(self):
        return self.name


class ProductHistory(models.Model):
    product = models.ForeignKey(Product)
    timestamp = models.DateTimeField()
    price = models.DecimalField(decimal_places=2, max_digits=9)
    alcohol_price = models.DecimalField(decimal_places=2, max_digits=9)

    class Meta:
        unique_together = ("product", "timestamp")
        get_latest_by = 'timestamp'

    def __str__(self):
        return '{}_{}'.format(self.product, self.timestamp)
