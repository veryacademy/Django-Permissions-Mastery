from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Project(models.Model):

    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse("project:project_detail", args=[self.slug])

    class Meta:
        permissions = [("can_add_new_project", "can add new project")]

    def __str__(self):
        return self.name
