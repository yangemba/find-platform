from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

def user_photo_directory_path(object, filename):
    filename = 'logo.{0}'.format(filename.split('.')[-1]) if '.' in filename else 'logo'

    return 'image_storage_{0}/{1}'.format(object.id, filename)


class User(AbstractUser):
    username = models.CharField(max_length=24,
                                unique=True, null=False)
    uuid = models.UUIDField('Unique UserID', unique=True, default=uuid.uuid4,
                             editable=False)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)





class UserFace(models.Model):
    user = models.ForeignKey(User, related_name="avatar",
                             on_delete=models.CASCADE, blank=True, null=True)
    photo = models.ImageField(upload_to=user_photo_directory_path, blank=True,
                              default="")

    def get_photo_url(self):
        new_photo = self.photo
        if not self.photo:
            new_photo = '/static/no_photo.jpg'
        return new_photo

