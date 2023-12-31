# Generated by Django 4.2.7 on 2023-12-23 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('video_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/', verbose_name='Картинка')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
            ],
            options={
                'verbose_name': 'Картинка',
                'verbose_name_plural': 'Картинка',
            },
        ),
        migrations.CreateModel(
            name='Pos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('text', models.TextField(max_length=250, verbose_name='Текст')),
                ('slug', models.SlugField(unique=True, verbose_name='Ссылка')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата')),
                ('publish', models.BooleanField(default=False, verbose_name='Публикация')),
                ('video', models.FileField(upload_to='videos/', verbose_name='Видео')),
                ('featured', models.BooleanField(default=False, verbose_name='Рекомендованные')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('gallery', models.ManyToManyField(related_name='posts', to='video_app.image', verbose_name='Галерея')),
                ('preview', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='video_app.image', verbose_name='Обложка')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
            },
        ),
        migrations.RemoveField(
            model_name='video',
            name='uploaded_by',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
