from django.db import models

class Vacancy(models.Model):
    title = models.CharField(max_length=300)
    company = models.CharField(max_length=300)
    requirements = models.TextField()
    salary = models.IntegerField()
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    contact = models.CharField(max_length=150, default='None')

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Vacancies'

    def __str__(self):
        return self.title