from django.db import models

# Create your models here.
class UrlHead(models.Model):
    url_env = models.CharField(max_length=10)
    url_domain = models.CharField(max_length=50)
    url_port = models.CharField(max_length=10)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.url_env

class UrlBody(models.Model):
    url_name = models.TextField(default='default_string')
    url_path = models.TextField()
    url_params = models.TextField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.url_path