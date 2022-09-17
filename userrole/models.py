from django.db import models
from django.contrib.auth import  get_user_model
User = get_user_model()

class RolesToAccess(models.Model):
    name=models.CharField(max_length=100)

    def  __str__(self):
        return self.name

class RolesDefine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(RolesToAccess , on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    


