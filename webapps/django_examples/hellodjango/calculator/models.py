from django.db import models

# Create your models here.

levels = (
    ("low", "low"),
    ("medium", "medium"),
    ("high", "high"),
)

class Prioritet(models.Model):
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=20, choices=levels)

    def __str__(self):
        return f"Prioritet: {self.name} | {self.level}"

class Calculation(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    operation = models.CharField(max_length=5)
    created = models.DateTimeField(auto_now=True)
    prioritet = models.ForeignKey(Prioritet, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return f"Calculation: {self.x} | {self.y} | {self.operation}"