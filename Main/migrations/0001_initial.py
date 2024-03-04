# Generated by Django 5.0.3 on 2024-03-04 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [""]

    operations = [
        migrations.CreateModel(
            name="EmailTable",
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
                ("Email",
                 models.EmailField(max_length=254, verbose_name="آدرس ایمیل")),
                ("Salary", models.CharField(max_length=10,
                                            verbose_name="حقوق")),
                ("Created", models.DateTimeField(auto_now_add=True)),
                ("Modified", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "EmailTable",
                "verbose_name_plural": "EmailTables",
            },
        ),
    ]
