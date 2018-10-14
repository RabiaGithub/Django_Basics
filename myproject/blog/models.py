from django.db import models

# Create your models here.

class Post(models.Model):
    title= models.CharField(max_length=140)
    body=models.TextField()
    date=models.DateTimeField()
    def __str__(self):
        return self.title
    

'''
##for metadata purposes for eg. if you want it for reference post (i.e. to list down your all posts smwhere)
## or all post titles
title is  actually an object of class  Post (Post.title)
'''

    

# with above str it is converting it into string otherwise it would have returned title's maybe address


