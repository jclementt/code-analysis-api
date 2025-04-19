from django.db import models
from analyzer.models.code_model import Code


class Analysis(models.Model):
    code = models.ForeignKey(Code, related_name='analysis', on_delete=models.CASCADE)
    complexity = models.IntegerField()
    number_lines = models.IntegerField()
    comments = models.IntegerField()

    def __str__(self):
        return f"Analise do código {self.code.id}"