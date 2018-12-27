from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.db.models.signals import pre_save


class Book(models.Model):
    book_name = models.CharField(max_length=100)
    author_name = models.ForeignKey('Author', on_delete=models.CASCADE, null=True)

    BOOK_STATUS = (
        ('p', 'Published'),
        ('u', 'Unpublished')
    )

    status = models.CharField(max_length=1, choices=BOOK_STATUS, default='p')
    cost = models.FloatField(max_length=5)
    currency = models.CharField(max_length=10)
    publish_date_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.book_name)


class Author(models.Model):
    author_name = models.CharField(max_length=50)
    subgenre_name = models.ForeignKey('SubGenre', on_delete=models.CASCADE, null=True)
    author_rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    about_author = models.TextField(max_length=500)

    def __str__(self):
        return str(self.author_name)


class Genre(models.Model):
    genre_name = models.CharField(max_length=50, unique=False)
    genre_details = models.CharField(max_length=100)
    slug = models.SlugField(unique=False)

    class Meta:
        ordering = ['genre_name']

    def __str__(self):
        return str(self.genre_name)


def pre_save_genre(sender, instance, *args, **kwargs):
    slug = slugify(instance.genre_name)
    flag = Genre.objects.filter(slug=slug).exists()
    if flag:
        slug = "%s-%s" % (slug, instance.id)
    else:
        instance.slug = slug


pre_save.connect(pre_save_genre, sender=Genre)


class SubGenre(models.Model):
    subgenre_name = models.CharField(max_length=50, null=True)
    genre_name = models.ForeignKey('Genre', on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=500)
    slug = models.SlugField(unique=False)

    def __str__(self):
        return str(self.subgenre_name)


def pre_save_subgenre(sender, instance,*args, **kwargs):
    slug = slugify(instance.subgenre_name)
    flag = SubGenre.objects.filter(slug=slug).exists()
    if flag:
        slug = "%s-%s" % (slug, instance.id)
    else:
        instance.slug = slug


pre_save.connect(pre_save_subgenre, sender=SubGenre)
