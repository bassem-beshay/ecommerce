from django.db import models


class Suber(models.Model):
    admin_id = models.BigAutoField(primary_key=True)
    fname = models.CharField(max_length=50)
    password = models.BigIntegerField()

    class Meta:
        db_table = 'suber'

    def __str__(self):
        return self.fname


class Client(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    address = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = 'client'

    def __str__(self):
        return self.user_name


class Category(models.Model):
    category_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    imgc = models.ImageField(upload_to='category_images', blank=True, null=True)
    admin = models.ForeignKey(Suber, on_delete=models.CASCADE, default=1)  # فرض قيمة افتراضية للمستخدم الأول

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class Color(models.Model):
    color_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=25)
    img = models.ImageField(upload_to='color_images', blank=True, null=True)
    admin = models.ForeignKey(Suber, on_delete=models.CASCADE, default=1)  # فرض قيمة افتراضية للمستخدم الأول

    class Meta:
        db_table = 'color'

    def __str__(self):
        return self.name


class Product(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=600)
    img = models.ImageField(upload_to='product_images', blank=True, null=True)
    price = models.BigIntegerField()
    admin = models.ForeignKey(Suber, on_delete=models.CASCADE, default=1)  # فرض قيمة افتراضية للمستخدم الأول
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    design = models.CharField(max_length=400, blank=True, null=True)
    detail = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name


class ProductColor(models.Model):
    pc_id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)  # فرض قيمة افتراضية للمنتج
    color = models.ForeignKey(Color, on_delete=models.CASCADE, default=1)  # فرض قيمة افتراضية للون

    class Meta:
        db_table = 'product_color'

    def __str__(self):
        return f'{self.product.name} - {self.color.name}'


class ProductUser(models.Model):
    pu_id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_user'

    def __str__(self):
        return f'{self.product.name} - {self.user.user_name}'
