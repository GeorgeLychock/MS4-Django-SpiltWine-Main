from django.db import models
from django.contrib.auth.models import User
from products.models import Wine


class CellarItem(models.Model):
    cellar_wine_pk = models.ForeignKey(Wine, null=True,
                                       blank=True, on_delete=models.CASCADE)
    user_id = models.IntegerField(null=True, blank=True)
    date_added_to_cellar = models.DateTimeField(auto_now_add=True)
    quantity_onhand = models.IntegerField(null=True, blank=True)

    def get_wine_name(self):
        return self.cellar_wine_pk
