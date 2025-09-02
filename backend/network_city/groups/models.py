from django.db import models


class Groups(models.Model):
    group_name = models.CharField(max_length=50)
    group_years = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания группы"
    )
    group_specialisation = models.CharField(max_length=100)

    def get_year(self):
        return self.group_years.year