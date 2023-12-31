# Generated by Django 4.2.3 on 2023-08-09 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_before_entry_ladders_health_check_checklist_before_entry_ladders_health_check_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='before_entry_remark',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='before_exit_bag_check',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='before_exit_remark',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='before_exit_tools_and_equipments_check',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='ladders_placement_check',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='material_deposited_in_required_area',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='work_place_orderliness',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
