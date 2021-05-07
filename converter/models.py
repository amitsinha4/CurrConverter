from django.db import models

# Create your models here.


class CurrencyList(models.Model):
    """ List of Currency """
    currency = models.CharField(max_length=100)
    currency_code = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=10)

    def __str__(self):
        return self.currency

    class Meta:
        db_table = 'currency_list'
