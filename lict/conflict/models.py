from django.db import models

class Article(models.Model):
    pmc = models.IntegerField(null=True)
    pmid = models.IntegerField(null=True)
    title = models.CharField(max_length=250)

class Organisation(models.Model):
    name = models.CharField(max_length=250)

class Conflict(models.Model):
    article = models.ForeignKey(Article)
    organisation = models.ForeignKey(Organisation)
