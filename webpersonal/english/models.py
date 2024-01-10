from django.db import models

# Create your models here.
class ProjectEnglish(models.Model):
    title = models.CharField(max_length=200, verbose_name="title")
    description = models.TextField(verbose_name="description")
    image = models.ImageField(verbose_name="image", upload_to="projects")
    link = models.URLField(null=True, blank=True, verbose_name="URL")
    created = models.DateTimeField(auto_now_add=True, verbose_name="created")
    updated = models.DateTimeField(auto_now=True, verbose_name="updated")

    class Meta:
        verbose_name = 'ProyectoIngles'
        verbose_name_plural = 'ProyectosIngles'

    def __str__(self):
        return self.title