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

class Image(models.Model):
    image=models.ImageField(upload_to ='images/', blank = True)
    name=models.CharField(max_length =30)
    caption=models.TextField(blank=True,null=True)
    profile=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    pub_date=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    likes=models.IntegerField(blank=True,null=True)
    # comments=models.ForeignKey(Comment)

    # def __str__(self):
    #     return self.name

    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()


    def update_caption(self,caption):
        self.caption = caption
        self.save()


    @classmethod
    def get_photos(cls):
        photos=cls.objects.all()
        return photos

    @classmethod
    def get_image_by_id(cls,image_id):
        image=cls.objects.get(id=image_id)
        return image
