from django.db import models
from django.utils import timezone


# This is a Post object. using Class to define an object.
# Post is a name of a model. Always start with a uppercase.
class Post(models.Model):
    author =  models.ForeignKey('auth.User')

    # These are properties that model Post has
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # publish method !
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


