# Generated by Django 5.1.1 on 2025-03-13 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_post_image_upload_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='text',
        ),
    ]
