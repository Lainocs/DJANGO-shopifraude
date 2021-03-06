# Generated by Django 4.0.3 on 2022-03-04 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_article_created_at_remove_article_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='price',
            field=models.FloatField(),
        ),
    ]
