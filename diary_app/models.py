from django.db import models

class DiaryCtg(models.Model):
    ctg_name = models.CharField(max_length=40)

    def __str__(self):
        return self.ctg_name


class DiaryModel(models.Model):
    name = models.CharField(max_length=200)
    diary_text = models.TextField()
    date = models.DateTimeField(auto_now_add=True, blank=True)
    diary_ctg = models.ForeignKey(DiaryCtg, on_delete=models.CASCADE)

    def __str__(self):
        return self.name