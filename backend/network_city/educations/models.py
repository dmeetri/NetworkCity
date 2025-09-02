from django.db import models
from users.models import Users, Teachers
from groups.models import Groups

class Subjects(models.Model):
    subject_name = models.CharField(max_length=100)
    subject_desc = models.TextField()

class GroupSubjects(models.Model):
    group_id = models.ForeignKey(Groups, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teachers, on_delete=models.CASCADE)

class Grades(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    group_subject_id = models.ForeignKey(GroupSubjects, on_delete=models.CASCADE)
    grade = models.CharField(max_length=50)
    grade_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата выставления оценки"
    )

class Attendance(models.Model):
    group_subject_id = models.ForeignKey(GroupSubjects, on_delete=models.CASCADE)
    grade_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата"
    )
    att_status = models.CharField(max_length=2) #ОП УП Н Б

class Timetables(models.Model):
    group_subject_id = models.ForeignKey(GroupSubjects, on_delete=models.CASCADE)
    timetable_date = models.DateTimeField(verbose_name="Дата")
    lession_number = models.IntegerField(max_length=2)
    room = models.IntegerField(max_length=4)
    start_time = models.DateTimeField(verbose_name="Дата начала")
    end_time = models.DateTimeField(verbose_name="Дата конца света")