from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.

class Image(models.Model):
    """"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='images_created',
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500, blank=True)
    url = models.URLField(max_length=500)
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True, db_index=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='images_liked',
                                        blank=True)

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):                ###FIX  slugify для русского текста
        """Автоматическая генерация слага"""        ###FIX
        if not self.slug:                           ###FIX
            self.slug = slugify(self.title)         ###FIX
        super(Image, self).save(*args, **kwargs)    ###FIX


    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])




