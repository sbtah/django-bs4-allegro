from django.db import models
from django.urls import reverse
from .utils import get_misioo_product


class Link(models.Model):

    url = models.URLField()

    article_name = models.CharField(max_length=220, blank=True)
    article_id = models.CharField(max_length=40, blank=True)
    article_sku = models.CharField(
        max_length=100, blank=True)
    current_price = models.FloatField(blank=True)

    old_price = models.FloatField(default=0)
    price_difference = models.FloatField(default=0)

    main_picture = models.URLField(blank=True)
    product_description = models.TextField(blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.article_name)

    def get_absolute_url(self):
        return reverse('links:product-detail', kwargs={
            'pk': self.pk,
        })

    class Meta:

        ordering = ('price_difference', '-created', )

    def save(self, *args, **kwargs):
        article_name, article_id, article_sku, article_price, main_picture, product_description = get_misioo_product(
            self.url)
        old_price = self.current_price

        if self.current_price:
            if article_price != old_price:
                diff = article_price - old_price
                self.price_difference = round(diff, 2)
                self.old_price = old_price

        else:
            self.old_price = 0
            self.price_difference = 0

        self.article_name = article_name
        self.article_id = article_id
        self.article_sku = article_sku
        self.current_price = article_price
        self.main_picture = main_picture
        self.product_description = product_description

        super().save(*args, **kwargs)
