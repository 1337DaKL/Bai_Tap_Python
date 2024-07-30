from django.db import models


class Post(models.Model):
    SHIRT_SIZES = {
        "S": "Small",
        "M": "Medium",
        "L": "Large",
    }
    title = models.CharField(max_length=200, null=False, blank=False)
    content = models.TextField(choices=SHIRT_SIZES)
