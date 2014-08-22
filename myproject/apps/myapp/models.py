from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=50)

    def __unicode__(self):
    	return self.title
