from django.db import models


class PredResults(models.Model):

    # zapisuje do bazy danych predykcje
    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()
    #HUJ = models.TextField()
    classification = models.CharField(max_length=30)

    def __str__(self):
        return self.classification
