# Generated by Django 4.2.1 on 2023-07-26 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anim', '0003_anime_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('Смотрю', 'Смотрю'), ('Просмотрено', 'Просмотрено'), ('Бросил', 'Бросил')], default='Просмотрено', max_length=250)),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=5)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('description', models.TextField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MyAnime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ranobe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('Смотрю', 'Смотрю'), ('Просмотрено', 'Просмотрено'), ('Бросил', 'Бросил')], default='Просмотрено', max_length=250)),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=5)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('description', models.TextField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='anime',
            old_name='studios',
            new_name='studio',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='author',
        ),
        migrations.AddField(
            model_name='dubbing',
            name='description',
            field=models.TextField(default='No description provided'),
        ),
        migrations.AddField(
            model_name='genre',
            name='description',
            field=models.TextField(default='No description provided'),
        ),
        migrations.AlterField(
            model_name='anime',
            name='dubbing',
            field=models.ManyToManyField(related_name='%(class)ss', to='anim.dubbing'),
        ),
        migrations.AlterField(
            model_name='anime',
            name='genres',
            field=models.ManyToManyField(related_name='%(class)ss', to='anim.genre'),
        ),
        migrations.AlterField(
            model_name='anime',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='dubbing',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='AnimeName',
        ),
        migrations.AddField(
            model_name='ranobe',
            name='dubbing',
            field=models.ManyToManyField(related_name='%(class)ss', to='anim.dubbing'),
        ),
        migrations.AddField(
            model_name='ranobe',
            name='genres',
            field=models.ManyToManyField(related_name='%(class)ss', to='anim.genre'),
        ),
        migrations.AddField(
            model_name='ranobe',
            name='studio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='anim.studio'),
        ),
        migrations.AddField(
            model_name='myanime',
            name='anime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myanime', to='anim.anime'),
        ),
        migrations.AddField(
            model_name='myanime',
            name='manga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myanime', to='anim.manga'),
        ),
        migrations.AddField(
            model_name='myanime',
            name='ranobe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myanime', to='anim.ranobe'),
        ),
        migrations.AddField(
            model_name='myanime',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myanime', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='manga',
            name='dubbing',
            field=models.ManyToManyField(related_name='%(class)ss', to='anim.dubbing'),
        ),
        migrations.AddField(
            model_name='manga',
            name='genres',
            field=models.ManyToManyField(related_name='%(class)ss', to='anim.genre'),
        ),
        migrations.AddField(
            model_name='manga',
            name='studio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='anim.studio'),
        ),
        migrations.AddField(
            model_name='comment',
            name='anime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='anim.anime'),
        ),
        migrations.AddField(
            model_name='comment',
            name='manga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='anim.manga'),
        ),
        migrations.AddField(
            model_name='comment',
            name='ranobe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='anim.ranobe'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
