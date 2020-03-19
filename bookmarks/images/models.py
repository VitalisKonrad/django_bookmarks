from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse

class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created', on_delete=models.CASCADE) #При удалении пользователя все его картинки удалятся
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True) #Для семантических url`ов
    url = models.URLField() #Ссылка на оригинал
    image = models.ImageField(upload_to='images/%Y/%m/%d/') #Сам файл
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True, db_index=True)#По этому полю создается индекс в БД
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='images_liked',
                                        blank=True)

    def __str__(self):
        return self.title

    #Переопределяем метод save. Сохраняем по слагу, если его нет, то по заголовку
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)

    def get_absolute_url(self):
            return reverse('images:detail', args=[self.id, self.slug])