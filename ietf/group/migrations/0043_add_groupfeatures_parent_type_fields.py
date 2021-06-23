# Generated by Django 2.2.19 on 2021-04-13 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('name', '0023_change_stream_descriptions'),
        ('group', '0042_add_liaison_contact_roles_to_used_roles'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupfeatures',
            name='parent_types',
            field=models.ManyToManyField(blank=True, help_text='Group types allowed as parent of this group type', related_name='child_features', to='name.GroupTypeName'),
        ),
        migrations.AddField(
            model_name='groupfeatures',
            name='need_parent',
            field=models.BooleanField(default=False, help_text='Does this group type require a parent group?', verbose_name='Need Parent'),
        ),
        migrations.AddField(
            model_name='groupfeatures',
            name='default_parent',
            field=models.CharField(blank=True, default='', help_text='Default parent group acronym for this group type', max_length=40, verbose_name='Default Parent'),
        ),
    ]