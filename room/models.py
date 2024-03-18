from django.db import models


class Rooms_type(models.Model):
    type = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Category slug',
                            unique=True)


class Rooms(models.Model):
    name = models.CharField(max_length=255)
    type_id = models.ForeignKey(Rooms_type, on_delete=models.CASCADE, related_name='images')
    capacity = models.IntegerField()

