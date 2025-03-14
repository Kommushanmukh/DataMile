from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=10, choices=[('student', 'Student'), ('mentor', 'Mentor')])
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Links post to logged-in user
    project_description = models.TextField()
    github_link = models.URLField()
    doubt_description = models.TextField()
    code_part = models.TextField()
    image_upload = models.ImageField(upload_to='media/post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when post is created

    def __str__(self):
        return f"{self.user.username} - {self.project_description[:30]}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()  # This field must exist
    created_at = models.DateTimeField(auto_now_add=True)



