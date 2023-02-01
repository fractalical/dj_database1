from django.db import models
from django.urls import reverse


class Phone(models.Model):
    name = models.CharField(max_length=50, null=False)
    price = models.FloatField(null=False)
    image = models.CharField(max_length=250)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=50)

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})
