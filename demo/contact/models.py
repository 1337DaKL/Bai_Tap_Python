from django.db import models


class contactForm (models.Model):
    username = models.CharField(max_length=50)
    passworld = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f'Tai khoan : {self.username} \n Mat Khau : {self.passworld}'
