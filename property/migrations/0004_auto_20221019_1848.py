# Generated by Django 2.2.24 on 2022-10-19 15:48

from django.db import migrations


def fill_new_building(apps, _):
    apps.get_model('property', 'Flat').objects.filter(construction_year__gte=2015).update(new_building=True)
    apps.get_model('property', 'Flat').objects.filter(construction_year__lt=2015).update(new_building=False)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(fill_new_building),
    ]
