# Generated by Django 4.2.3 on 2023-09-04 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='pastryrecipe',
            name='category',
            field=models.CharField(choices=[('CC', 'Cakes and Cupcakes'), ('PT', 'Pies and Tarts'), ('CB', 'Cookies and Biscuits'), ('PP', 'Pastries and Puff Pastry'), ('FD', 'Frozen Desserts'), ('PC', 'Puddings and Custards'), ('FR', 'Fruit-based Desserts'), ('ID', 'International Desserts'), ('OT', 'Other Desserts')], default='OT', max_length=2),
        ),
        migrations.AddField(
            model_name='pastryrecipe',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
