from django.db import models


class Qradardb(models.Model):
    logsource = models.TextField(blank=False)
    sigma_name = models.TextField(blank=True)
    dec = models.TextField(blank=True)
    name = models.TextField(blank=True)
    sigma_condition = models.TextField(blank=True)
    qradar_condition = models.TextField(blank=True)
    tactics = models.TextField(blank=True)
    techinque = models.TextField(blank=True)
