from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,null = True,on_delete=models.CASCADE,related_name = "profile")
    profile_photo=models.ImageField(upload_to='profiles',blank=True)
    bio=models.TextField()

    def __str__(self):
        return self.user

    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()

    def update_bio(self,bio):
        self.bio = bio
        self.save()

    @classmethod
    def get_profile_by_id(cls,image_id):
        profile=cls.objects.get(id=profile_id)
        return profile

    @classmethod
    def search_by_user(cls,search_term):
        instagram=cls.objects.filter(user__username=search_term)
        return instagram
