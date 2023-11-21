from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=300)
    price = models.CharField(max_length=300)
    image = models.CharField(max_length=300)
    release_date = models.CharField(max_length=300)
    lte_exists = models.CharField(max_length=300)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return (f'{self.name} '
                f'{self.price} ' 
                f'{self.image} '
                f'{self.release_date} '
                f'{self.lte_exists} '
                f'{self.slug}')
