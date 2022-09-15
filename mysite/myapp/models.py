from django.db import models


class TrusteeCodeLegend(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "trustee_code_legend"

    def __str__(self):
        return "{}".format(
            self.name
        )
