# Generated by Django 5.0.1 on 2024-02-03 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Records",
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
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("first_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
                ("email", models.CharField(max_length=255)),
                ("phone_no", models.CharField(max_length=200)),
                ("role", models.CharField(max_length=200)),
                ("country", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("branch", models.CharField(max_length=150)),
            ],
        ),
    ]