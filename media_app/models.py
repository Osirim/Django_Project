from django.db import models

class Multimedia(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    media_file = models.FileField(upload_to='media/')
    media_type = models.CharField(max_length=50, choices=[
        ('image', 'Image'),
        ('video', 'Video'),
        ('audio', 'Audio'),
    ])
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
