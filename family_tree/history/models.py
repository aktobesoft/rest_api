from django.db import models

class Pedigree(models.Model):
    name = models.CharField(verbose_name="Есімі", max_length=150)
    parent = models.ForeignKey('self', verbose_name="Әкесі", blank=True, null=True, related_name='Child', on_delete=models.CASCADE)
    level = models.IntegerField(verbose_name="Деңгей") 

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.parent and self.level != self.parent.level:
            self.level = self.parent.level + 1
            super().save(*args, **kwargs)
            # тут нужно еще иерархию уровни пересчитать, где нубудь в функции
        elif not self.parent and self.level!=0:
            self.level = 0
            # тут нужно еще иерархию уровни пересчитать, где нубудь в функции


