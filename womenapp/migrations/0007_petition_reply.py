# Generated by Django 4.2.4 on 2024-03-10 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('womenapp', '0006_remove_advocateregistration_lawyertype_petition'),
    ]

    operations = [
        migrations.AddField(
            model_name='petition',
            name='reply',
            field=models.CharField(max_length=100, null=True),
        ),
    ]