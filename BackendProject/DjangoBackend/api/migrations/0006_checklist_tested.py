# Generated by Django 4.2.4 on 2023-09-11 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_checklist_before_entry_remark_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklist',
            name='tested',
            field=models.BooleanField(default=None, null=True),
        ),
    ]
