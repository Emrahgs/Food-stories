from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    image = models.ImageField('Image', upload_to='profile_pictures', null=True, blank=True)
    bio = models.TextField('Bio', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def profile_picture(self):
        if self.image:
            return self.image.url
        return 'https://www.pngfind.com/pngs/m/470-4703547_icon-user-icon-hd-png-download.png'

    def get_absolute_url(self):
        return reverse_lazy('accounts:user_profile', kwargs={'pk': self.id})