import imp
from tortoise.models import Model
from tortoise import fields


class Mentor(Model):
    name = fields.CharField(max_length=255)
    username = fields.CharField(max_length=100)
    bio = fields.TextField()

    class PydanticMeta:
        exclude = ("id", )
        
    def __str__(self):
        return self.name