from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.

class TextDocument(models.Model):
    title = models.CharField('Title', max_length=200, unique=True)
    text = CKEditor5Field('Text', config_name='extends')
    author = models.CharField(max_length=50)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-dateUpdated','-dateCreated']

    def __str__(self):
        return self.title