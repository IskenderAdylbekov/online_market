from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse
from unidecode import unidecode


CustomUser = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=200)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="product_image/%Y/%m/%d", blank=True, null=True)
    created_by = models.ForeignKey(
        CustomUser, related_name="products", on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    subcategory = models.ForeignKey(
        "Subcategory",
        related_name="products",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk, "slug": self.slug})

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["name"]),
            models.Index(fields=["created_at"]),
        ]

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)


class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        related_name="subcategories",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name_plural = "Subcategories"
        verbose_name = "Subcategory"

    def __str__(self) -> str:
        return self.name
