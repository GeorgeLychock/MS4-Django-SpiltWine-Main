import uuid

from tabnanny import verbose
from django.db import models


# model Classes are in order of proper database ingestion
class Appellation(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    # class methods borrowed from Code Institute
    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Region(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    location = models.CharField(max_length=254, null=True, blank=True)
    # attrib setting from Code Institute, if a value is deleted in this table set value to NULL in other tables
    appellation = models.ForeignKey('Appellation', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class WineType(models.Model):

    class Meta:
        verbose_name_plural = 'Wine Types'

    name = models.CharField(max_length=30)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class WineBrand(models.Model):

    class Meta:
        verbose_name_plural = 'Wine Brands'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class WineAccessoryBrand(models.Model):

    class Meta:
        verbose_name_plural = 'Wine Accessory Brands'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
        
        
class CulinaryBrand(models.Model):

    class Meta:
        verbose_name_plural = 'Culinary Brands'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class CountryState(models.Model):

    class Meta:
        verbose_name_plural = 'Countries States'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    region = models.ForeignKey('Region', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Varietal(models.Model):
    name = models.CharField(max_length=30)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)
    wine_type = models.ForeignKey('WineType', null=True, blank=True, on_delete=models.SET_NULL)
    img_file_name = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    wiki_url = models.URLField(max_length=1024, null=True, blank=True)
    alt_url_1 = models.URLField(max_length=1024, null=True, blank=True)


    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Style(models.Model):
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Body(models.Model):

    class Meta:
        verbose_name_plural = 'Body'

    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Measure(models.Model):

    name = models.CharField(max_length=20)
    friendly_name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
        

# Create base product fields
class Product(models.Model):
    name = models.CharField(max_length=254)
    sku = models.CharField(max_length=254, null=True, blank=True)
    puid = models.CharField(max_length=64, null=False, editable=False)
    image = models.ImageField(null=True, blank=True)
    img_url = models.URLField(max_length=1024, null=True, blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    size = models.DecimalField(max_digits=6, decimal_places=2)
    measure = models.ForeignKey('Measure', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField()
    featured = models.BooleanField(null=False, blank=False, default=False)

    class Meta:
        abstract = True

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()
            
            
class Wine(Product):
    vintage = models.IntegerField(null=True, blank=True)
    brand = models.ForeignKey('WineBrand', null=True, blank=True, on_delete=models.SET_NULL)
    country_state = models.ForeignKey('CountryState', null=True, on_delete=models.SET_NULL)
    region = models.ForeignKey('Region', null=True, blank=True, on_delete=models.SET_NULL)
    appellation = models.ForeignKey('Appellation', null=True, blank=True, on_delete=models.SET_NULL)
    wine_type = models.ForeignKey('WineType', null=True, on_delete=models.SET_NULL)
    varietal = models.ForeignKey('Varietal', null=True, on_delete=models.SET_NULL)
    style = models.ForeignKey('Style', null=True, on_delete=models.SET_NULL)
    abv = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    taste = models.TextField(max_length=100, null=True, blank=True)
    body = models.ForeignKey('Body', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class WineAccessory(Product):

    class Meta:
        verbose_name_plural = 'Wine Accessory Products'

    brand = models.ForeignKey('WineAccessoryBrand', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Culinary(Product):

    class Meta:
        verbose_name_plural = 'Culinary Products'

    brand = models.ForeignKey('CulinaryBrand', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name