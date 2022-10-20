# Generated by Django 4.1.2 on 2022-10-20 07:28

from django.db import migrations
import phonenumbers


def fill_owner_pure_phone(apps, _):
    for flat in apps.get_model('property', 'Flat').objects.all():
        try:
            parsed_phonenumber = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        except phonenumbers.phonenumberutil.NumberParseException:
            continue

        if not phonenumbers.is_valid_number(parsed_phonenumber):
            continue

        if not phonenumbers.is_possible_number(parsed_phonenumber):
            continue

        flat.owner_pure_phone = phonenumbers.format_number(
            parsed_phonenumber,
            phonenumbers.PhoneNumberFormat.INTERNATIONAL
        )
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20221020_1019'),
    ]

    operations = [
        migrations.RunPython(fill_owner_pure_phone),
    ]