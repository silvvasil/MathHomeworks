from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
	name = models.CharField('Название работы', max_length=120)
	description = models.TextField(blank=True)
	deadline = models.DateTimeField('Дедлайн сдачи работы')
	
	def __str__(self):
		return self.name


class Work(models.Model):
	task = models.ForeignKey(Task, blank=True, null=True, on_delete=models.SET_NULL)
	description = models.TextField(blank=True)
	comment = models.TextField(blank=True)
	owner = models.IntegerField("Work Owner", blank=False, default=1)
	work_image = models.ImageField(null=True, blank=True, upload_to="images/")

	def __str__(self):
		user = User.objects.filter(id=self.owner)[0]
		# user = list(User.objects.all())[self.owner - 1]
		# print(user.first_name, user.last_name)
		return str(self.task) + "  работу сдал " + user.first_name + " " + user.last_name
		# return str(self.task) + "  работу сдал " + str(self.owner)