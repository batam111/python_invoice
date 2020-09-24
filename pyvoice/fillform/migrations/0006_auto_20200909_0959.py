# Generated by Django 3.1 on 2020-09-09 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fillform', '0005_auto_20200909_0519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice_detail',
            name='logoname',
        ),
        migrations.AddField(
            model_name='invoice_detail',
            name='client_Address',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='invoice_detail',
            name='client_Email',
            field=models.EmailField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='invoice_detail',
            name='client_Name',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='invoice_detail',
            name='client_Phone',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='invoice_detail',
            name='date',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='invoice_detail',
            name='invoice_Number',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='invoice_detail',
            name='subtotal',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='invoice_detail',
            name='table_Items',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='invoice_detail',
            name='tax',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='invoice_detail',
            name='terms',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='invoice_detail',
            name='total',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
