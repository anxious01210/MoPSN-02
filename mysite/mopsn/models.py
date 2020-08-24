from django.db import models
import datetime

# Create your models here.

class Ps4(models.Model):
    """docstring for Ps4."""

    games = models.TextField(blank=True)
    image = models.ImageField(upload_to="mopsn/images", blank=True)
    price_paypal = models.DecimalField(max_digits=5, decimal_places=2)
    price_btc = models.DecimalField(max_digits=5, decimal_places=2)
    region_code = models.IntegerField(blank=True, null=True)
    region_country = models.CharField(blank=True, max_length=30)
    publish_date = models.DateTimeField(blank=True, default=datetime.datetime.now)
    sold = models.BooleanField(default=False)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Netflix(models.Model):
    """docstring for Netflix."""

    image = models.ImageField(upload_to="mopsn/images", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price_paypal = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    price_btc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    language = models.CharField(default='English', blank=True, null=True, max_length=30)
    publish_date = models.DateTimeField(blank=True, null=True, default=datetime.datetime.now)
    sold = models.BooleanField(default=False)

    THREE_MONTH = '3-M'
    SIX_MONTH = '6-M'
    TWELVE_MONTH = '12-M'

    ACCOUNT_PERIOD_CHOICES = [
        (THREE_MONTH, 'Three_month'),
        (SIX_MONTH, 'Six_month'),
        (TWELVE_MONTH, 'Twelve_month'),
    ]
    account_period = models.CharField(
        max_length=4,
        choices=ACCOUNT_PERIOD_CHOICES,
        default=THREE_MONTH,
    )

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

# class Nety(models.Model):
#     """docstring for Netflix."""
#
#     name = models.CharField(blank=True, max_length=100)
#     # image = models.ImageField(upload_to="mopsn/images", blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#
#     def __str__(self):
#         return self.name
