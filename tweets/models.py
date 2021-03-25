from django.db import models


# Tweet Model
class Tweet(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    image = models.FileField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.content
