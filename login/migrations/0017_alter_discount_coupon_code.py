# Generated by Django 4.0.2 on 2022-05-15 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0016_alter_discount_offer_ammount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='Coupon_Code',
            field=models.CharField(max_length=20),
        ),
    ]
