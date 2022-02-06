from django.db import models
from products.models import Wine

class CellarItem(models.Model):
    cellar_wine_pk = models.ForeignKey(Wine, null=True, blank=True, on_delete=models.CASCADE)
    cellar_user_pk = models.CharField(max_length=254)
    date_added_to_cellar = models.DateTimeField(null=True, blank=True)
    quantity_onhand = models.IntegerField(null=True, blank=True)

    def get_wine_name(self):
        return self.cellar_wine_pk

