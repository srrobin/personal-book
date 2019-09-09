from django.db import models




class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title



class PhoneBookModel(models.Model):
    name = models.CharField(max_length=100)
    personal_number = models.CharField(max_length=15)
    home_number = models.CharField(max_length=15)
    office_number = models.CharField(max_length=15)
    email = models.EmailField()
    about_person = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/',blank=True,null=True)


    def __str__(self):
        return self.name

