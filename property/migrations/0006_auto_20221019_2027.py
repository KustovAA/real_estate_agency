# Generated by Django 2.2.24 on 2022-10-19 17:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_complain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complains', to='property.Flat', verbose_name='Квартира, на которую пожаловались'),
        ),
        migrations.AlterField(
            model_name='complain',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complains', to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался?'),
        ),
    ]