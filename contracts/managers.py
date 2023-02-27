from datetime import timezone
from django.db import models


class ContractManager(models.Manager):
    def all(self):
        return self.get_queryset()
