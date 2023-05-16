import logging
from django.db import models
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)

class Blog(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    owner = models.ForeignKey(
        User, related_name="blogs", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        logger.info('Saving blog post %s', self.title)
        super().save(*args, **kwargs)
