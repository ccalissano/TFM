from django.db import models

# Create your models here.
class ratings(models.Model):
     book_id=models.IntegerField()
     user_id=models.IntegerField()
     rating=models.IntegerField()
     
class books(models.Model):
    id=models.IntegerField(primary_key=True)
    book_id=models.IntegerField()
    best_book_id=models.IntegerField()
    work_id=models.IntegerField()
    books_count=models.IntegerField()
    isbn=models.CharField(max_length=255)
    isbn13=models.CharField(max_length=255)
    authors=models.CharField(max_length=1000)
    original_publication_year=models.CharField(max_length=255)
    original_title=models.CharField(max_length=255)
    title=models.CharField(max_length=255)
    language_code=models.CharField(max_length=255)
    average_rating=models.CharField(max_length=255)
    ratings_count=models.IntegerField()
    work_ratings_count=models.IntegerField()
    work_text_reviews_count=models.IntegerField()
    ratings_1=models.IntegerField()
    ratings_2=models.IntegerField()
    ratings_3=models.IntegerField()
    ratings_4=models.IntegerField()
    ratings_5=models.IntegerField()
    image_url=models.CharField(max_length=255)
    small_image_url=models.CharField(max_length=255)
    
   