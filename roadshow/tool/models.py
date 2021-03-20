from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=20)
    rank = models.CharField(max_length=5)

class Plan_of_insntruction(models.Model):
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    lessons = models.IntegerField(default=0)

# The following are psql tables copied from amundy's orginal project and translated to Django ORM
# Still need to set up relations
class Blocks(models.Model):
    hours = models.FloatField()
    max_enrl_blk = models.IntegerField()
    min_enrl_blk = models.IntegerField()
    prep_time_hours_blk = models.FloatField()
    # retraining_interval_blk INT,
	#  safety_related_blk VARCHAR(1),
    security_class_id = models.CharField(max_length=10)
    #-student_materials_blk VARCHAR(256)
    block_number = models.CharField(max_length=2)
    block_desc = models.CharField(max_length=256)

class Units(models.Model):
    unit_number = models.IntegerField()
    unit_description = models.CharField(max_length=256)
    # student_materials_unit VARCHAR(2000),
    # a_v_aids VARCHAR(2000),
    # assignment VARCHAR(2000),
    # attention VARCHAR(2000),
    # motivation VARCHAR(2000),
    # review VARCHAR(2000),
    # overview VARCHAR(2000),
    # transition VARCHAR(2000),
    # summary VARCHAR(2000),
    # remotivation VARCHAR(2000),
    # closure VARCHAR(2000),

class Objectives(models.Model):
    application = models.CharField(max_length=1000)
    evaluation = models.CharField(max_length=1000)
    inst_guidance = models.CharField(max_length=1000)
    # --instructor_materials_obj = models.CharField(max_length=256),
    # --measurement_obj = models.CharField(max_length=20),
    # --mir_desc = models.CharField(max_length=1000),
    # --mir_hours INT,
    # --mir_num INT,
    # --mir_type = models.CharField(max_length=1),
    objective_hours = models.FloatField()
    objective_statement = models.CharField(max_length=2000),
    # --operational = models.CharField(max_length=1),
    # --prep_time_hours_obj INT,
    # --safety_related_obj = models.CharField(max_length=1),
    # --security_class_id INT,
    # --training_type INT,
    unit_number = models.CharField(max_length=2)
    # --objective_letter VARCHAR(2)

class Tasks(models.Model):
    task_desc = models.CharField(max_length=2000)
    task_number = models.IntegerField()
    parent_id = models.IntegerField()

# Original sql script can be found at https://github.com/amundy14/Expo_demo/blob/main/databaseInit.sql
