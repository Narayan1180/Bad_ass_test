from django.db import models

# Create your models here.
class MondayIntegration(models.Model):

    board_id = models.CharField(
        max_length=50,
        unique=True
    )

    board_name = models.CharField(
        max_length=200
    )

    access_token = models.TextField()

    webhook_id = models.CharField(
        max_length=100
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

class FranchiseDevelopment(models.Model):


    monday_item_id = models.CharField(
        max_length=50,
        unique=True
    )

    franchise_name = models.CharField(
        max_length=255
    )

    market = models.CharField(
        max_length=100,
        blank=True
    )

    stage = models.CharField(
        max_length=50
    )

    loi_date = models.DateField(
        null=True,
        blank=True
    )

    under_contract_date = models.DateField(
        null=True,
        blank=True
    )

    under_development_date = models.DateField(
        null=True,
        blank=True
    )

    open_date = models.DateField(
        null=True,
        blank=True
    )

    approved_date = models.DateField(
        null=True,
        blank=True
    )

    hold_date = models.DateField(
        null=True,
        blank=True
    )

    monday_created_at = models.DateTimeField(null=True,blank=True)

    monday_updated_at = models.DateTimeField(null=True,blank=True)

    synced_at = models.DateTimeField(
        auto_now=True
    )