from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    
    def absolute_get_url(self):
        return reverse('flearn:category_detail', args=[self.slug])
    

class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name='sub_categories',
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='sub_category/intro', blank=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def absolute_get_url(self):
        return reverse('flearn:subcategory_detail', args=[self.slug])


class Course(models.Model):
    sub_category = models.ForeignKey(SubCategory, related_name='courses',
                                    on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='course/intro', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def absolute_get_url(self):
        return reverse('flearn:course_detail', args=[self.slug])


class Video(models.Model):
    course = models.ForeignKey(Course, related_name='videos',
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    video = models.FileField(upload_to='course/video')

    def __str__(self):
        return self.name