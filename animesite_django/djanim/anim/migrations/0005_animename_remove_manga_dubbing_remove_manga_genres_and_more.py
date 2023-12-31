# Generated by Django 4.2.3 on 2023-07-28 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anim', '0004_comment_manga_myanime_ranobe_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimeName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.RemoveField(
            model_name='manga',
            name='dubbing',
        ),
        migrations.RemoveField(
            model_name='manga',
            name='genres',
        ),
        migrations.RemoveField(
            model_name='manga',
            name='studio',
        ),
        migrations.RemoveField(
            model_name='myanime',
            name='anime',
        ),
        migrations.RemoveField(
            model_name='myanime',
            name='manga',
        ),
        migrations.RemoveField(
            model_name='myanime',
            name='ranobe',
        ),
        migrations.RemoveField(
            model_name='myanime',
            name='user',
        ),
        migrations.RemoveField(
            model_name='ranobe',
            name='dubbing',
        ),
        migrations.RemoveField(
            model_name='ranobe',
            name='genres',
        ),
        migrations.RemoveField(
            model_name='ranobe',
            name='studio',
        ),
        migrations.RenameField(
            model_name='anime',
            old_name='studio',
            new_name='studios',
        ),
        migrations.RemoveField(
            model_name='dubbing',
            name='description',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='description',
        ),
        migrations.AddField(
            model_name='anime',
            name='author',
            field=models.CharField(default='Anonymous', max_length=100),
        ),
        migrations.AlterField(
            model_name='anime',
            name='dubbing',
            field=models.ManyToManyField(related_name='animes', to='anim.dubbing'),
        ),
        migrations.AlterField(
            model_name='anime',
            name='genres',
            field=models.ManyToManyField(related_name='animes', to='anim.genre'),
        ),
        migrations.AlterField(
            model_name='anime',
            name='rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, 'Five')], default=5),
        ),
        migrations.AlterField(
            model_name='dubbing',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Manga',
        ),
        migrations.DeleteModel(
            name='MyAnime',
        ),
        migrations.DeleteModel(
            name='Ranobe',
        ),
        migrations.AlterField(
            model_name='anime',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anim.animename'),
        ),
    ]
