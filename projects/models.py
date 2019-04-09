from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(blank=True, null=True)

    @property
    def image_url(self):
    	if self.image and hasattr(self.image, 'url'):
    		return self.image.url

    def __str__(self):
    	return self.title
