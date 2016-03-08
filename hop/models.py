from django.db import models

class Aroma(models.Model):
    label = models.CharField(max_length=255)

    def __str__(self):
        return self.label

class Hop(models.Model):
    USAGE_CHOICES = (
        ('AROM', "Aroma"),
        ('BITT', "Bittering"),
        ('BOTH', "Aroma and Biterring")
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    usage = models.CharField(choices=USAGE_CHOICES, max_length=4)
    year = models.PositiveIntegerField()

    aroma = models.ManyToManyField(Aroma, related_name='hops')

    oil_amount = models.FloatField(default=0)
    geraniol = models.FloatField(default=0)
    humulene = models.FloatField(default=0)
    farnesene = models.FloatField(default=0)
    caryophyllene = models.FloatField(default=0)
    linalool = models.FloatField(default=0)
    myrcene = models.FloatField(default=0)
    pinene = models.FloatField(default=0)

    alpha_acid = models.FloatField(default=0)
    beta_acid = models.FloatField(default=0)

    def __str__(self):
        return self.name
