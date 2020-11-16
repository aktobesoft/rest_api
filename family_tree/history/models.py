from django.db import models

class pedigree(models.Model):
    name = models.CharField("Атасы",max_length=150)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='Баласы', on_delete=models.CASCADE)
    level = models.IntegerField("Уровень")    