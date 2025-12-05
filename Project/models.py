from django.db import models

# Модель "Производитель" (Manufacturer)
class Manufacturer(models.Model):
    manufacturer_id = models.AutoField(primary_key=True)  # Код_производителя
    name = models.CharField(max_length=255)  # Наименование

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'manufacturer'


# Модель "Марка" (Brand)
class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)  # Код_марки
    brand_name = models.CharField(max_length=255)  # Название_марки

    def __str__(self):
        return self.brand_name

    class Meta:
        db_table = 'brand'


# Модель "Вид сладости" (SweetType)
class SweetType(models.Model):
    type_id = models.AutoField(primary_key=True)  # Код_вида
    type_name = models.CharField(max_length=255)  # Название_вида

    def __str__(self):
        return self.type_name

    class Meta:
        db_table = 'sweet_type'


# Модель "Вкус" (Flavor)
class Flavor(models.Model):
    flavor_id = models.AutoField(primary_key=True)  # Код_вкуса
    flavor_name = models.CharField(max_length=255)  # Название_вкуса

    def __str__(self):
        return self.flavor_name

    class Meta:
        db_table = 'flavor'


# Модель "Сладость" (Sweet)
class Sweet(models.Model):
    sweet_id = models.AutoField(primary_key=True)  # Код_сладости
    type = models.ForeignKey(SweetType, on_delete=models.CASCADE)  # Код_вида
    flavor = models.ForeignKey(Flavor, on_delete=models.CASCADE)  # Код_вкуса
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)  # Код_марки
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)  # Код_производителя
    weight = models.CharField(max_length=50)  # Вес (строка, так как может быть "100г" или "0.5кг")
    price = models.IntegerField()  # Цена
    photo = models.CharField(max_length=255, blank=True, null=True)  # Фото (путь к файлу)
    composition = models.TextField(blank=True, null=True)  # Состав

    def __str__(self):
        return f"Sweet #{self.sweet_id}"

    class Meta:
        db_table = 'sweet'


# Модель "Покупка" (Purchase)
class Purchase(models.Model):
    purchase_id = models.AutoField(primary_key=True)  # Код_покупки
    sweet = models.ForeignKey(Sweet, on_delete=models.CASCADE)  # Код_сладости
    quantity = models.IntegerField()  # Количество
    amount = models.IntegerField()  # Сумма
    purchase_date = models.DateField()  # Дата_покупки

    def __str__(self):
        return f"Purchase #{self.purchase_id} on {self.purchase_date}"

    class Meta:
        db_table = 'purchase'