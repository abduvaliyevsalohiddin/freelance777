# Generated by Django 5.0.4 on 2025-05-09 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_skill_freelancerskill_alter_job_skills_required'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='freelancerskill',
            name='skill',
        ),
        migrations.RemoveField(
            model_name='freelancerskill',
            name='user',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
        migrations.DeleteModel(
            name='FreelancerSkill',
        ),
    ]
