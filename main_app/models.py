from django.db import models
from django.urls import reverse
from datetime import date, datetime
from django.contrib.auth.models import User 
# Create your models here.


class Subforum(models.Model): 
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    pinned = models.BooleanField(default=False)
    content = models.TextField(max_length=600)
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )

    def __str__(self): 
        return f'title of this subforum: {self.title}'
    
    def get_absolute_url(self): 
        return reverse('subforums_detail', kwargs={'subforum_id': self.id})  #refactor with the correct views reference and variable names 
    
class Subforum_Likes(models.Model): 
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )
    subforum = models.ForeignKey(
        Subforum, 
        on_delete=models.CASCADE
    )

    def __str__(self): 
        return f'likes model {self.id} '

    
class Post(models.Model): 
    content = models.TextField(max_length=600)
    date = models.DateField(auto_now_add=True)
    subforum = models.ForeignKey(
        Subforum, 
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )
  
    def __str__(self):
        return f'the id of this post is {self.id}'
    
    def get_absolute_url(self): 
        return reverse('subforums_detail', kwargs={'subforum_id': self.subforum.id}) 

    class Meta: 
        ordering = ['-date']

class Photo(models.Model): 
    url = models.CharField(max_length=200)
    subforum = models.ForeignKey(
        Subforum, 
        on_delete=models.CASCADE
        )
    

    def __str__(self):
        return f'photo id: {self.id} @{self.url}'



class Comment(models.Model): 
    content = models.TextField(max_length=250)
    date = models.DateField(auto_now_add=True)
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'comment id: {self.id}'

    class Meta: 
        ordering = ['-date']

class Company(models.Model): 
    name =  models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    url = models.CharField(max_length=150, verbose_name='Company Job Postings URL')
    industry = models.CharField(max_length=100)
    photo_url = models.CharField(max_length=150)

    def __str__(self): 
        return f'{self.name}'
    
    def get_absolute_url(self): 
        return reverse('company_detail', kwargs={'pk': self.id})  #refactor with the correct views reference and variable names 
    

class Company_Subforum(models.Model): 
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    pinned = models.BooleanField(default = False)
    content = models.TextField(max_length=600)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
        )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )

    def __str__(self): 
        return f'title subforum: {self.title}'
    
    def get_absolute_url(self): 
        return reverse('company_subforums_detail', kwargs={
            'company_id': self.company_id,
            'company_subforum_id': self.id
            })  #refactor with the correct views reference and variable names 

class Company_Subforum_Likes(models.Model): 
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )
    subforum = models.ForeignKey(
        Company_Subforum, 
        on_delete=models.CASCADE
    )

    def __str__(self): 
        return f'likes model {self.id} '
    
class Company_Post(models.Model): 
    content = models.TextField(max_length=600)
    date = models.DateField(auto_now_add=True)
    subforum = models.ForeignKey(
        Company_Subforum, 
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )
  
    def __str__(self):
        return f'post id: {self.id}'

    class Meta: 
        ordering = ['-date']

class Company_Comment(models.Model): 
    content = models.TextField(max_length=250)
    date = models.DateField(auto_now_add=True)
    post = models.ForeignKey(
        Company_Post, 
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )
    def __str__(self):
        return f'comment id: {self.id}'

    class Meta: 
        ordering = ['-date']

class Company_Photo(models.Model): 
    url = models.CharField(max_length=200)
    subforum = models.ForeignKey(
        Company_Subforum, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Photo id: {self.id} @{self.url}'
    
class Job_Application(models.Model): 
    
    STATUS_CHOICES = (
        ('applied', 'Applied'), 
        ('will_apply', 'Will Apply'), 
        ('heard_back', 'Heard Back'), 
        ('interview', 'Interviewing'), 
        ('offered', 'Offered'), 
        ('rejected', 'Rejected'), 
        ('ghosted', 'Ghosted')
    )

    role = models.CharField(max_length=150)
    url = models.CharField(max_length=250)
    company = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    salary = models.CharField(max_length=100) 
    date = models.DateField('Date')
    location = models.CharField(max_length=100) 
    status = models.CharField(
        max_length=50, 
        choices=STATUS_CHOICES, 
        default='applied'
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )

    def __str__(self): 
        return self.role
    
    def get_absolute_url(self): 
        return reverse('applications_detail', kwargs= {'user_id': self.user_id, 'application_id': self.id} )
    
class Application_Component(models.Model): 
    type = models.CharField(max_length=150)
    date = models.DateField('Date')
    contact = models.CharField(max_length=200) 
    description = models.TextField(max_length=500)
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )
    application = models.ForeignKey(
        Job_Application, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'note id: {self.id}'
    
    class Meta: 
        ordering = ['-date']
    

class Component_Note(models.Model): 
    content = models.TextField(max_length=400)
    date = models.DateField(auto_now_add=True)
    component = models.ForeignKey(
        Application_Component, 
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'note id: {self.id}'

    class Meta: 
        ordering = ['-date']

    
class Pdf(models.Model): 
    url = models.CharField(max_length=200)
    job_application = models.ForeignKey(
        Job_Application, 
        on_delete=models.CASCADE
        )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'PDF for job_application: {self.job_application_id} @{self.url}'