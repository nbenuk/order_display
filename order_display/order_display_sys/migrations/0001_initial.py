# Generated by Django 4.0.3 on 2022-04-02 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_ref', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
