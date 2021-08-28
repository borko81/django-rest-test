from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=30, verbose_name='Name')
    password = models.CharField(max_length=10, verbose_name='Password')
    email = models.EmailField(verbose_name='Email')
    date_created = models.DateTimeField(verbose_name='Date Created', auto_now_add=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=40, verbose_name='Title')
    description = models.CharField(max_length=100, verbose_name='Description')
    client_name = models.CharField(max_length=100, verbose_name='Client Name')

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    description = models.CharField(max_length=100, verbose_name='Description')
    time_elapsed = models.IntegerField(verbose_name='Elapsed Time', null=True, default=None, blank=True)
    importance = models.IntegerField(verbose_name='Importance')
    project = models.ForeignKey(Project, verbose_name='Project', null=True, blank=True, default=None,
                                on_delete=models.CASCADE)
    app_user = models.ForeignKey(UserProfile, verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Supervisor(UserProfile):
    specialisation = models.CharField(max_length=50, verbose_name='Specialization')

    def __str__(self):
        return self.specialisation


class Developer(UserProfile):
    specialisation = models.CharField(max_length=50, verbose_name='Developer')
