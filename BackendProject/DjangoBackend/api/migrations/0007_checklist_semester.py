# Generated by Django 4.2.4 on 2023-09-11 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_checklist_tested'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklist',
            name='semester',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no'), ('none', 'none')], default='none', max_length=20),
        ),
    ]
