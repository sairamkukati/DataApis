from django.db import models


class BaseModel(models.Model):
    """Abstract Model with name field"""
    name = models.CharField(max_length=120, blank=True)

    class Meta:
        abstract = True

class Location(BaseModel):
    """Model that represents Locations"""
    
    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"
        db_table = "data_locations"
        ordering = ["name",]

    def __str__(self):
        return self.name

class Department(BaseModel):
    """Model that represents Department
    
    Fields: id, name, location
    """
    location = models.ForeignKey(Location, related_name="departments", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"
        db_table = "data_departments"
        ordering = ["name",]

    def __str__(self):
        return self.name

class Category(BaseModel):
    """Model that represents Category 
    
    Fields: id, name, department
    """
    department = models.ForeignKey(Department, related_name="categories", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        db_table = "data_categories"
        ordering = ["name",]

    def __str__(self):
        return self.name

class SubCategory(BaseModel):
    """Model that represents SubCategory  
    
    Fields: id, name, category
    """
    category  = models.ForeignKey(Category, related_name="subcategories", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "SubCategory"
        verbose_name_plural = "SubCategories"
        db_table = "data_subCategories" 
        ordering = ["name",]

    def __str__(self):
        return self.name

    
class SKU(models.Model):
    """ Model that represents Stock keep Units (SKUs)
    
    fields: id, name, description
    """
    sku = models.IntegerField(unique=True, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    subcategory = models.ForeignKey(
        SubCategory, related_name="skus", on_delete=models.CASCADE
    ) 
    class Meta:
        verbose_name = "SKU"
        verbose_name_plural = "SKUs"
        db_table = "data_sku" 
        ordering = ["sku",]

    def __str__(self):
        return self.description