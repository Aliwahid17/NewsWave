# Generated by Django 4.1.7 on 2023-04-11 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('news', '0003_alter_newsarticle_comments_alter_newsarticle_likes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='likes',
            field=models.ManyToManyField(related_name='Likes', to='user.profile'),
        ),
    ]