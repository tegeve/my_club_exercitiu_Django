# Generated by Django 4.1 on 2022-08-11 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0005_alter_event_manager"),
    ]

    operations = [
        migrations.RenameField(
            model_name="venue", old_name="email_adress", new_name="email_address",
        ),
    ]
