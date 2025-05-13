from django.db import models

class Blogpost(models.Model):
    class Publish_status(models.TextChoice):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'published', 'Published'
        ARCHIVED = 'archived', 'Archived'
        
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20,choices=Publish_status.choices,
    default=Publish_status.DRAFT)   
    excerpt = models.TextField(max_length=200, blank
    =True)

    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title 

        

