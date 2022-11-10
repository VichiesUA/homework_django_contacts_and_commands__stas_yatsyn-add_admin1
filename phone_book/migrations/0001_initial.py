# Generated by Django 4.1.1 on 2022-10-10 11:55

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PhoneBook",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("phone", models.SlugField(max_length=100)),
                ("birthday_date", models.DateField()),
                ("create_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("is_auto_generated", models.BooleanField(default=False)),
            ],
        ),
    ]
