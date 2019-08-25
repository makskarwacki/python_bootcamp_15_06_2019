from django.db import models
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey("authors.Author", on_delete=models.CASCADE)
    cover = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"Book {self.title} - {self.author}"

