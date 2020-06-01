from django.test import TestCase
from .models import Profile, Post


# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile = Profile(user="suad", name = 'samar', profile_pic = '')
        self.profile.save()

    def tearDown(self):
        Profile.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

class PostTestClass(TestCase):
    def setUp(self):
        self.post = Post(image = 'samar', caption = "suad' post")
        self.post.save()

    def tearDown(self):
        Post.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))