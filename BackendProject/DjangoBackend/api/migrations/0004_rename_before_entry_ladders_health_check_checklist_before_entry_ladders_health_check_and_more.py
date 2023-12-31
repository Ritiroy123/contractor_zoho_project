# Generated by Django 4.2.3 on 2023-08-09 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_worker_name_checklist_worker_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checklist',
            old_name='Before_entry_ladders_health_check',
            new_name='before_entry_ladders_health_check',
        ),
        migrations.RenameField(
            model_name='checklist',
            old_name='Before_entry_safety_helmet_check',
            new_name='before_entry_safety_helmet_check',
        ),
        migrations.RenameField(
            model_name='checklist',
            old_name='Before_entry_safety_shoes_check',
            new_name='before_entry_safety_shoes_check',
        ),
        migrations.RenameField(
            model_name='checklist',
            old_name='Before_entry_tobacco_and_alcohol',
            new_name='before_entry_tobacco_and_alcohol',
        ),
        migrations.RenameField(
            model_name='checklist',
            old_name='Material_deposited_in_required_area',
            new_name='material_deposited_in_required_area',
        ),
        migrations.RenameField(
            model_name='checklist',
            old_name='Mental_health',
            new_name='mental_health',
        ),
        migrations.RenameField(
            model_name='checklist',
            old_name='Work_place_orderliness',
            new_name='work_place_orderliness',
        ),
    ]
