from django.db import models
from django.utils import timezone


class Album(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('closed', 'Closed'),
        ('admin', 'Admin'),
    )

    title = models.CharField(max_length=20)
    author = models.CharField(max_length=10)

    cover = models.ImageField(upload_to='cover')
    location = models.URLField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-publish',)


class Episode(models.Model):
    title = models.CharField(max_length=200)
    script_count = models.IntegerField(default=0)
    mp3_count = models.IntegerField(default=0)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
