# Generated by Django 3.2.4 on 2021-10-12 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarjeta', '0003_alter_tarjeta_folio_tarjeta'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='telefono',
            field=models.CharField(max_length=10, null=True, verbose_name='Telefono'),
        ),
    ]
