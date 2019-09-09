from django.db import models

class AlbumModel(models.Model):
    title = models.TextField()
    img = models.ImageField(upload_to='album/', blank=True, null=True)

    def __str__(self):
        return self.title
