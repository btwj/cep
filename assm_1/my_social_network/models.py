from django.db import models
from django.contrib.auth.models import User

class UserLink(models.Model):
  from_user = models.ForeignKey(User, related_name="from_user")
  to_user = models.ForeignKey(User, related_name="to_user")
  date_added = models.DateField()
  
  def __unicode__(self):
    return self.from_user.get_username() + " is following " + self.to_user.get_username()
  
  def save(self, *args, **kwargs):
    if (self.from_user == self.to_user):
      return
    super(UserLink, self).save(*args, **kwargs)
    
  class Meta:
    unique_together = ('from_user', 'to_user')
  
  