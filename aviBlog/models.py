from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Author(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email_address= models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Tag(models.Model):
    caption= models.CharField(max_length=20)

    def __str__(self):
        return f"{self.caption}"

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=250)
    image_name = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author= models.ForeignKey(Author,null=True, on_delete=models.SET_NULL, related_name="posts")
    tags= models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title} by {self.author}"
    
class Comment(models.Model):
    user_name=models.CharField(max_length=20)
    user_email=models.EmailField()
    text= models.TextField(max_length=405)
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"{self.user_name} commented {self.text}"
    
