import uuid as uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class CustomUser(models.Model):
    user = models.OneToOneField(User, db_column='user', on_delete=models.CASCADE)
    uuid = models.UUIDField(db_column="uuid", unique=True, default=uuid.uuid4, editable=False)
    dob = models.DateField(db_column="dob", max_length=50, null=True, blank=True)
    gender = models.CharField(db_column="gender", max_length=50, null=True, blank=True)
    picture_path = models.CharField(db_column="picture_path", max_length=200, null=True, blank=True)
    phone_no = models.CharField(db_column="mobile_no", max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_column="created_at")
    updated_at = models.DateTimeField(auto_now=True, db_column="updated_at")

    def __str__(self):
        return f"{self.user.email}"  # Assuming User has an email field.

    @staticmethod
    @receiver(post_save, sender=User)
    def create_additional_user_data_for_user(sender, instance, created, **kwargs):
        if created:
            CustomUser.objects.create(user=instance)


class ActivityLogs(models.Model):
    ACTIVITY_LIST = {
        '0': "created",
        '1': "deleted',"
    }
    action = models.IntegerField(choices=ACTIVITY_LIST, db_column='action')
    points = models.IntegerField(db_column="Points", null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_column="created_at")
    updated_at = models.DateTimeField(auto_now=True, db_column="updated_at")

    def __str__(self):
        return f"Points: {self.points}"


class SecurityInformation(models.Model):
    two_factor_auth = models.BooleanField(db_column="Two Factor Auth", default=False, null=True, blank=True)
    last_password_change_at = models.DateTimeField(db_column="Last Password Change At", null=True, blank=True)
    reset_phone_no = models.CharField(db_column="reset_mobile_no", max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_column="created_at")
    updated_at = models.DateTimeField(auto_now=True, db_column="updated_at")

    def __str__(self):
        return f"auth: {self.two_factor_auth}"


class UserPreference(models.Model):
    language = models.CharField(db_column="Language", default="en", max_length=50)
    theme = models.IntegerField(db_column="Theme", null=True, blank=True)
    time_zone = models.CharField(db_column="Time_Zone", null=True, default=True, max_length=100)
    notification_Preference = models.CharField(db_column="Notification_Preference", null=True, default=True,
                                               max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, db_column="created_at")
    updated_at = models.DateTimeField(auto_now=True, db_column="updated_at")

    def __str__(self):
        return f"Language: {self.language}"


class Country(models.Model):
    country_name = models.CharField(db_column="Country_name", max_length=30)
    country_code = models.CharField(db_column="Country_code", max_length=20)
    country_tel_code = models.CharField(db_column="Country_tel_code", max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, db_column="created_at")
    updated_at = models.DateTimeField(auto_now=True, db_column="updated_at")

    def __str__(self):
        return f"country name: {self.country_name}"


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, db_column='user', on_delete=models.CASCADE)
    bio = models.CharField(db_column="bio", max_length=2000, blank=True, null=True)
    # activity_log = models.OneToOneField(ActivityLogs, db_column="activity_log", on_delete=models.CASCADE, default=1)
    # security_information = models.OneToOneField(SecurityInformation, db_column="security_information",
    #                                          on_delete=models.CASCADE, default=1)
    # user_preference = models.OneToOneField(UserPreference, db_column="user_preference", on_delete=models.CASCADE, default=1)
    # country = models.OneToOneField(Country, db_column="country", on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True, db_column="created_at")
    updated_at = models.DateTimeField(auto_now=True, db_column="updated_at")

    def __str__(self):
        return f"profile:{self.user} "

    @staticmethod
    @receiver(post_save, sender=CustomUser)
    def create_additional_user_data_for_user(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)


class Report(models.Model):
    REPORT_TYPES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]

    report_type = models.CharField(max_length=10, choices=REPORT_TYPES)
    generated_date = models.DateField(auto_now_add=True)
    total_bookings = models.IntegerField(default=0)
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    cancelled_bookings = models.IntegerField(default=0)
    active_buses = models.IntegerField(default=0)
    most_popular_route = models.CharField(max_length=255, null=True, blank=True)
    least_popular_route = models.CharField(max_length=255, null=True, blank=True)
    peak_booking_time = models.TimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, db_column="user", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.report_type.capitalize()} Report - {self.generated_date}"


class TotalReportSummary(models.Model):
    total_bookings = models.IntegerField(default=0)
    total_revenue = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    total_cancelled = models.IntegerField(default=0)
    total_buses = models.IntegerField(default=0)
    total_routes = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, db_column="user", on_delete=models.CASCADE)

    def __str__(self):
        return "Total Report Summary"
