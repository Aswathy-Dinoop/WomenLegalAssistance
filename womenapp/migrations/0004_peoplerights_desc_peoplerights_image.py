# Generated by Django 4.2.4 on 2024-03-05 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('womenapp', '0003_peoplerights'),
    ]

    operations = [
        migrations.AddField(
            model_name='peoplerights',
            name='desc',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='peoplerights',
            name='image',
            field=models.ImageField(max_length=50, null=True, upload_to=''),
        ),
    ]