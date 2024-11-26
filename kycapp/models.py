from django.db import models
import uuid

# Create your models here.
class GenderType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    gender_type = models.CharField(max_length=200)
    created_date_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.gender_type


class NameType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    gender = models.ForeignKey(GenderType, on_delete=models.CASCADE)
    name_type = models.CharField(max_length=255)
    created_date_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name_type}-{self.gender.gender_type}'


class FirstName(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_type = models.ForeignKey(NameType, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, unique=True)
    created_date_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=['first_name']),
        ]

    def __str__(self):
        return self.first_name


class MiddleName(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_type = models.ForeignKey(NameType, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=255)
    created_date_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=['middle_name']),
        ]

    def __str__(self):
        return self.middle_name


class LastName(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_type = models.ForeignKey(NameType, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=255)
    created_date_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=['last_name']),
        ]

    def __str__(self):
        return self.last_name


class EmailExtensions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email_extension_name = models.CharField(max_length=255, unique=True)
    created_date_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=['email_extension_name']),
        ]

    def __str__(self):
        return self.email_extension_name


class PhoneNumber(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mobile_number = models.CharField(max_length=10, unique=True)
    created_date_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_used = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=['mobile_number']),
        ]

    def __str__(self):
        return self.mobile_number


class Interests(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    interests = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.interests


class IndianNames(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=255)
    date_of_birth = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=10, unique=True)
    email = models.CharField(max_length=255, unique=True)
    genrated_in_month = models.IntegerField(default=0)
    disabled_for_month = models.BooleanField(default=False)
    disabled_on_month = models.DateTimeField(null=True, blank=True)
    genrated_in_year = models.IntegerField(default=0)
    disabled_for_year = models.BooleanField(default=False)
    disabled_on_year = models.DateTimeField(null=True, blank=True)
    voter_id_card = models.CharField(max_length=10, unique=True)
    created_date_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=['full_name']),
            models.Index(fields=['email']),
            models.Index(fields=['genrated_in_month', 'genrated_in_year']),
            models.Index(fields=['is_active']),
        ]

    def __str__(self):
        return self.full_name


class AvailableNames(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_id = models.ForeignKey(IndianNames, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=['name_id']),
            models.Index(fields=['is_active']),
        ]

    def __str__(self):
        return self.name_id.full_name
