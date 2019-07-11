from django.db import models
import datetime
from django.core.validators import URLValidator, MaxValueValidator, MinValueValidator
from django.utils.translation import gettext as _


class Operator(models.Model):

    EMAIL = "Email"
    MAIL = "Mail"

    BREEDER = "BREEDER"
    SELLER = "SELLER"
    BOTH = "BREEDER & SELLER"
    OPERATION_TYPE_CHOICES = (
        (BREEDER, "BREEDER"),
        (SELLER, "SELLER"),
        (BOTH, "BREEDER & SELLER"),
    )

    description = _("An operator is a seller/breeder of cats and/or dogs")
    reg_num = models.CharField("Operator REG #", max_length=14)
    first_name = models.CharField(max_length=32)
    middle_name = models.CharField(max_length=50, default="", blank=True)
    last_name = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=50, default="", blank=True)
    email_address = models.CharField(max_length=50, default="", blank=True)
    create_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)
    CONTACT_METHOD_CHOICE = ((EMAIL, "email"), (MAIL, "mail"))
    comm_pref = models.CharField("Communication method",
        max_length=10, choices=CONTACT_METHOD_CHOICE, default=EMAIL
    )
    operation_type = models.CharField(
        max_length=20, choices=OPERATION_TYPE_CHOICES, default=BREEDER
    )

    operation_name = models.CharField(max_length=50, default="", blank=True)
    operation_URL = models.CharField(max_length=50, default="", blank=True)
   

    def __str__(self):
        return "Reg ID: \t %s %s , %s" % (self.reg_num, self.last_name, self.first_name)

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.regNum)
        super().save(*args, **kwargs)
        self.reg_num = "BC-DCBR-" + str(self.pk).zfill(6)
        super().save()

    # self.regNum = 'BC ' + str(self.kwargs['pk'])

    class Meta:
        verbose_name_plural = "Operators"
        verbose_name = "Operators : breeders and sellers"


class Address(models.Model):
    PRIMARY = "PRI"
    OPERATION = "OPN"
    TYPE_CHOICES = (
        (PRIMARY, "Primary"),
        (OPERATION, "Operation"),
    )
    type = models.CharField(max_length=3, choices=TYPE_CHOICES, default=PRIMARY)
    street_num = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    suite = models.CharField(max_length=32, default="", blank=True)
    street_name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    postal_code = models.CharField(max_length=7)
    province = models.CharField(max_length=2, default="BC")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    operator = models.ForeignKey(
        Operator,
        on_delete=models.CASCADE,
        related_name="addresses",
        related_query_name="addresses",
    )

    def __str__(self):
        return self.street_name


    def save(self, *args, **kwargs):
        # self.operator = self.operator
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Addresses"


class Risk_Factor_Operation(models.Model):

    TATTOO = "TATTOO"
    MICROCHIP = "MICROCHIP"
    OTHER = "OTHER"
    PERMANENT_ID_CHOICES = (
        (TATTOO, "TATTOO"),
        (MICROCHIP, "MICROCHIP"),
        (OTHER, "OTHER"),
    )

    DOG = "DOG"
    CAT = "CAT"
    BOTH = "DOG & CAT"

    ANIMAL_TYPE_CHOICES = ((DOG, "DOG"), (CAT, "CAT"), (BOTH, "DOG & CAT"))
    accidental_breeding = models.BooleanField(default=False)
    num_workers = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    animal_type = models.CharField(
        max_length=10, choices=ANIMAL_TYPE_CHOICES, default=BOTH
    )
    num_breeds_dogs = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    num_breeds_cats = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    has_vet = models.BooleanField(default=False)
    has_perm_id = models.BooleanField(default=False)
    perm_id_type = models.CharField(
        max_length=10, choices=PERMANENT_ID_CHOICES, default=TATTOO
    )
    perm_id_other = models.CharField(max_length=10, default="", blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    operator = models.ForeignKey(
        Operator,
        on_delete=models.CASCADE,
        related_name="risk_factor_operations",
        related_query_name="risk_factor_operations",
    )

    def __str__(self):
        return "Operation risk for: \t %s " % (self.operator)

    def publish(self):
        "operator = breeder / seller"

    def save(self, *args, **kwargs):
        # self.operator = self.operator
        super().save(*args, **kwargs)
        self.reg_num = "BC-DCBR-" + str(self.pk).zfill(6)
        super().save()

    class Meta:
        verbose_name_plural = "RiskFactorOperations"


class Risk_Factor_Animal(models.Model):

    num_dogs_intact = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    num_litter_whelped = models.IntegerField(
        default=0, validators=[MinValueValidator(0)]
    )
    num_cats_intact = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    num_litter_queened = models.IntegerField(
        default=0, validators=[MinValueValidator(0)]
    )
    num_dog_sold = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    num_dog_transferred = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    num_dog_traded = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    num_dog_leased = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    num_cat_sold = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    num_cat_transferred = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    num_cat_traded = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    num_cat_leased = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    operator = models.ForeignKey(
        Operator,
        on_delete=models.CASCADE,
        related_name="risk_factor_animals",
        related_query_name="risk_factor_animals",
    )

    def __str__(self):
        return "Animal risk for: \t %s " % (self.operator)

    def save(self, *args, **kwargs):
        # self.operator = self.operator
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "RiskFactorAnimals"


class Association_Membership(models.Model):

    assoc_name = models.CharField(max_length=50, default="", blank=True)
    membership_num = models.CharField(max_length=20, default="", blank=True)
    assoc_URL = models.CharField(max_length=50, default="", blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    operator = models.ForeignKey(
        Operator, on_delete=models.CASCADE, related_name="associations"
    )

    def __str__(self):
        return self.assoc_name

    def save(self, *args, **kwargs):
        # self.operator = self.operator
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Associations"


class Inspection(models.Model):
    reg_num = models.CharField(max_length=14)
    op_first_name = models.CharField(max_length=32)
    op_middle_name = models.CharField(max_length=50)
    op_last_name = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    soc_1 = models.BooleanField(default=False)
    soc_2 = models.BooleanField(default=False)
    soc_3 = models.BooleanField(default=False)
    soc_4 = models.BooleanField(default=False)
    soc_5 = models.BooleanField(default=False)
    soc_6 = models.BooleanField(default=False)
    soc_7 = models.BooleanField(default=False)
    soc_8 = models.BooleanField(default=False)
    soc_9 = models.BooleanField(default=False)
    soc_10 = models.BooleanField(default=False)
    soc_11 = models.BooleanField(default=False)

    soc_1_comment = models.TextField(default="", blank=True)
    soc_2_comment = models.TextField(default="", blank=True)
    soc_3_comment = models.TextField(default="", blank=True)
    soc_4_comment = models.TextField(default="", blank=True)
    soc_5_comment = models.TextField(default="", blank=True)
    soc_6_comment = models.TextField(default="", blank=True)
    soc_7_comment = models.TextField(default="", blank=True)
    soc_8_comment = models.TextField(default="", blank=True)
    soc_9_comment = models.TextField(default="", blank=True)
    soc_10_comment = models.TextField(default="", blank=True)
    soc_11_comment = models.TextField(default="", blank=True)

    def __str__(self):
        return "Reg ID: \t %s %s , %s" % (
            self.reg_num,
            self.op_last_name,
            self.op_first_name,
        )

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Inspections"
