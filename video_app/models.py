from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your models here.
class Image(models.Model):
    image = models.ImageField('Картинка', upload_to = 'image/')
    title = models.CharField('Заголовок', max_length = 100)

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинка'

    def __str__(self):
        return self.title
    
class Pos(models.Model):
    author =  models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Автор')
    title = models.CharField('Заголовок', max_length = 100)
    text = models.TextField('Текст', max_length = 250)
    slug = models.SlugField('Ссылка', unique = True)
    preview = models.ForeignKey(Image, on_delete = models.SET_NULL, null = True, blank = True, verbose_name = 'Обложка')
    gallery =  models.ManyToManyField(Image, verbose_name = 'Галерея', related_name = 'posts')
    date = models.DateTimeField('Дата', default = timezone.now)
    publish =  models.BooleanField('Публикация', default = False)
    video = models.FileField('Видео', upload_to = 'videos/')
    featured =  models.BooleanField('Рекомендованные', default = False)

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def get_absolute_url(self):
        return reverse('post_detail_urls', kwargs = {'slug': self.slug})
    
    def __str__(self):
        return self.title