from django.db import models
from django.db.models import permalink

class Article(models.Model):
    pmc = models.IntegerField(null=True)
    pmid = models.IntegerField(null=True)
    title = models.CharField(max_length=250)
    raw_conflict_text = models.TextField()


class RealOrganisationManager(models.Manager):
    def get_query_set(self):
        return super(RealOrganisationManager, self).get_query_set().filter(is_a_real_organisation=True)


class Organisation(models.Model):
    name = models.CharField(max_length=250)
    is_a_real_organisation = models.BooleanField(default=True)

    objects = models.Manager()
    real_organisations = RealOrganisationManager()

    @permalink
    def get_absolute_url(self):
        return ('organisation', [str(self.id)])

    def __unicode__(self):
        return self.name


class Conflict(models.Model):
    article = models.ForeignKey(Article)
    organisation = models.ForeignKey(Organisation)

class Drug(models.Model):
    jeff_id = models.IntegerField()
    name = models.CharField(max_length=500)

class ArticleDrugs(models.Model):
    article = models.ForeignKey(Article)
    drug = models.ForeignKey(Drug)

class Mesh(models.Model):
    """
    What's a Mesh???
    """
    jeff_id = models.IntegerField()
    name = models.CharField(max_length=500)
