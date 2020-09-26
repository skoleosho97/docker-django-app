from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Course(models.Model):
    Fall_2020 = "FAL2020"
    Winter_2020 = "WIN2020"
    Spring_2021 = "SPR2021"
    Summer_2021 = "SUM2021"

    SEMESTER_CHOICES = [
        (Fall_2020, "Fall 2020"),
        (Winter_2020, "Winter 2020"),
        (Spring_2021, "Spring 2021"),
        (Summer_2021, "Summer 2021"),
    ]

    title = models.CharField(max_length=10, unique=True, null=False)
    slug = models.TextField(null=False)
    semester = models.CharField(
        max_length=7, choices=SEMESTER_CHOICES, default=Fall_2020
    )

    class Meta:
        ordering = ["-title"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return "{}, {}".format(self.title, self.semester)


class Post(models.Model):
    Fall_2020 = "FAL2020"
    Winter_2020 = "WIN2020"
    Spring_2021 = "SPR2021"
    Summer_2021 = "SUM2021"

    SEMESTER_CHOICES = [
        (Fall_2020, "Fall 2020"),
        (Winter_2020, "Winter 2020"),
        (Spring_2021, "Spring 2021"),
        (Summer_2021, "Summer 2021"),
    ]

    title = models.CharField(max_length=200, unique=True, null=False)
    slug = models.TextField(null=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="course_posts"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(null=False)
    categories = models.ManyToManyField("Category")

    class Meta:
        ordering = ["-created_on"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=50, null=False)

    class Meta:
        ordering = ["-title"]

    def __str__(self):
        return self.title
