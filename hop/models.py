from django.db import models

class Aroma(models.Model):
    label = models.CharField(max_length=255)

class Hop(models.Model):
    USAGE_CHOICES = (
        ('AROM', "Aroma"),
        ('BITT', "Bittering"),
        ('BOTH', "Aroma and Biterring")
    )
    aroma = models.ManyToManyField(Aroma)

    name = models.CharField(max_length=255)
    description = models.TextField()
    usage = models.CharField(choices=USAGE_CHOICES, max_length=4)
    year = models.DateField()

    oil_amount = models.PositiveIntegerField()
    geraniol = models.PositiveIntegerField()
    humulene = models.PositiveIntegerField()
    farnesene = models.PositiveIntegerField()
    caryophyllene = models.PositiveIntegerField()
    linalool = models.PositiveIntegerField()
    myrcene = models.PositiveIntegerField()
    pinene = models.PositiveIntegerField()

    alpha_acid = models.PositiveIntegerField()
    beta_acid = models.PositiveIntegerField()
