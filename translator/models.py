from django.db import models

# Create your models here.
class Translation(models.Model):
    session_key = models.CharField(max_length=40)
    text = models.TextField()
    translated_text = models.TextField()

    source_language = models.CharField(max_length=10)
    target_language = models.CharField(max_length=10)

    is_favorite = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.source_language} → {self.target_language}"