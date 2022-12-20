from django.db import models
    
class Sources(models.Model):
    
    url = models.URLField(max_length=128)
    name = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)

class BasicAuth(models.Model):
    
    basic_auth = models.OneToOneField(Sources, on_delete=models.CASCADE, related_name="basic_auth")
    login = models.CharField(max_length=30, default="")
    password = models.CharField(max_length=30, default="")

class RequestBody(models.Model):
    
    request_body = models.OneToOneField(Sources, on_delete=models.CASCADE, related_name="request_body")
    Request_id = models.CharField(max_length=128, default="")
    ClubId = models.CharField(max_length=128, default="")
    Method = models.CharField(max_length=128, default="")
    
class ParametersRequestBody(models.Model):
    
    Parameters = models.OneToOneField(RequestBody, on_delete=models.CASCADE, related_name="Parameters")
    ServiceId = models.CharField(max_length=30, default="", blank=True)
    