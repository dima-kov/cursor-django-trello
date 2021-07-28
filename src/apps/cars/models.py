from django.contrib.auth import get_user_model
from django.db import models

AUTH_USER_MODEL = get_user_model()


class Car(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_PUBLISHED = 'published'
    STATUS_SOLD = 'sold'
    STATUS_ARCHIVED = 'archived'

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending Car Sell"),
        (STATUS_PUBLISHED, "Published"),
        (STATUS_SOLD, "Sold"),
        (STATUS_ARCHIVED, "Archived"),
    )

    views = models.PositiveIntegerField(default=0, editable=False)
    slug = models.SlugField(max_length=75)
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
        blank=True
    )
    view = models.OneToOneField(
        'cars.CarView',
        on_delete=models.SET_NULL,
        null=True,
    )
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cars',
    )
    tags = models.ManyToManyField(
        'cars.CarTag',
    )

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машини'

    def __str__(self):
        return self.slug


class CarView(models.Model):
    color = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Car View'


class CarTag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Car Tag'
