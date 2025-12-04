from django.db import models

class Manufacturer(models.Model):
    """Модель производителя сладостей"""
    manufacturer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Manufacturer Name")
    
    def str(self):
        return self.name
    
    class Meta:
        db_table = 'Производитель'
        verbose_name = 'Manufacturer'
        verbose_name_plural = 'Manufacturers'


class Brand(models.Model):
    """Модель марки сладостей"""
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=255, verbose_name="Brand Name")
    
    def str(self):
        return self.brand_name
    
    class Meta:
        db_table = 'Марка'
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class SweetType(models.Model):
    """Модель вида сладостей (например: шоколад, конфеты, печенье)"""
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=255, verbose_name="Sweet Type")
    
    def str(self):
        return self.type_name
    
    class Meta:
        db_table = 'Вид_сладости'
        verbose_name = 'Sweet Type'
        verbose_name_plural = 'Sweet Types'


class Taste(models.Model):
    """Модель вкуса сладостей (например: шоколадный, фруктовый, ванильный)"""
    taste_id = models.AutoField(primary_key=True)
    taste_name = models.CharField(max_length=255, verbose_name="Taste")
    
    def str(self):
        return self.taste_name
    
    class Meta:
        db_table = 'Вкус'
        verbose_name = 'Taste'
        verbose_name_plural = 'Tastes'


class Sweet(models.Model):
    """Основная модель сладости с ссылками на связанные таблицы"""
    sweet_id = models.AutoField(primary_key=True)
    sweet_type = models.ForeignKey(
        SweetType, 
        on_delete=models.CASCADE, 
        verbose_name="Sweet Type",
        db_column='Код_вида'
    )
    taste = models.ForeignKey(
        Taste, 
        on_delete=models.CASCADE, 
        verbose_name="Taste",
        db_column='Код_вкуса'
    )
    brand = models.ForeignKey(
        Brand, 
        on_delete=models.CASCADE, 
        verbose_name="Brand",
        db_column='Код_марки'
    )
    manufacturer = models.ForeignKey(
        Manufacturer, 
        on_delete=models.CASCADE, 
        verbose_name="Manufacturer",
        db_column='Код_производителя'
    )
    weight = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Weight")
    price = models.IntegerField(verbose_name="Price")
    photo = models.CharField(max_length=255, verbose_name="Photo", blank=True, null=True)
    composition = models.TextField(verbose_name="Composition", blank=True, null=True)
    
    def str(self):
        return f"{self.brand} - {self.sweet_type} ({self.taste})"
    
    @property
    def total_weight(self):
        """Возвращает вес с единицами измерения (если не указаны)"""
        if self.weight and not any(char.isalpha() for char in self.weight):
            return f"{self.weight}г"
        return self.weight
    
    class Meta:
        db_table = 'Сладость'
        verbose_name = 'Sweet'
        verbose_name_plural = 'Sweets'
        indexes = [
            models.Index(fields=['sweet_type', 'brand']),
        ]


class Purchase(models.Model):
    """Модель покупки сладостей"""
    purchase_id = models.AutoField(primary_key=True)
    sweet = models.ForeignKey(
        Sweet, 
        on_delete=models.CASCADE, 
        verbose_name="Sweet",
        db_column='Код_сладости'
    )
    quantity = models.IntegerField(verbose_name="Quantity", default=1)
    amount = models.IntegerField(verbose_name="Total Amount")
    purchase_date = models.DateField(verbose_name="Purchase Date", auto_now_add=True)
    def str(self):
        return f"Purchase #{self.purchase_id} - {self.sweet}"
    def save(self, *args, **kwargs):
        """Автоматически рассчитывает сумму при сохранении на основе цены сладости и количества"""
        if not self.amount and self.sweet:
            self.amount = self.sweet.price * self.quantity
        super().save(*args, **kwargs)
    
    @property
    def unit_price(self):
        """Возвращает цену за единицу товара"""
        return self.sweet.price if self.sweet else 0
    
    class Meta:
        db_table = 'Покупка'
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'
        ordering = ['-purchase_date']