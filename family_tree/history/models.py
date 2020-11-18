from django.db import models
from history.mymodule import slugify

class Pedigree(models.Model):
    name = models.CharField(verbose_name="Есімі", max_length=150)
    parent = models.ForeignKey('self', verbose_name="Әкесі", blank=True, null=True, related_name='Child', on_delete=models.CASCADE)
    level = models.IntegerField(verbose_name="Деңгей") 
    slug = models.CharField(verbose_name="Идентификатор", max_length=150, blank=True, unique=True)

    readonly_fields = ["slug", "level"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.parent and self.level != self.parent.level + 1:
            self.level = self.parent.level + 1
            # тут нужно еще иерархию уровни пересчитать, где нубудь в функции
        elif not self.parent and self.level!=0:
            self.level = 0
            # тут нужно еще иерархию уровни пересчитать, где нубудь в функции
        if self.slug != slugify(self.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


