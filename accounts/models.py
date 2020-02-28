from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    """Get user info and image from form"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='images/default.jpg', upload_to='images')

    def __str__(self):
        return "{0} Profile".format(self.user.username)

    def save(self, *args, **kwargs):

        """retrieve image from profileUpdateForm"""
        img = Image.open(self.image)
       

        """
        image is stored with max width and height of 400,
        so large files don't take up a lot of storage space
        """
        if img.height > 400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.image)

        super(Profile, self).save(*args, **kwargs)
