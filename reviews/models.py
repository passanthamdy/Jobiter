from django.db import models

EMP_STATUS = (
    ("FULLTIME", "Full-Time"),
    ("PARTTIME", "Part-Time"),
    ("INTERN", "Internship"),

)


# Create your models here.
class Review(models.Model):
    company = models.ForeignKey("accounts.User", verbose_name="Company", on_delete=models.CASCADE,
                                related_name='review_company_id')
    reviewer = models.ForeignKey("accounts.User", verbose_name="Reviewer", on_delete=models.CASCADE,
                          related_name="review_employee_id")
    pros = models.TextField()
    # position = models.CharField(max_length=50)
    # title = models.CharField(max_length=50)
    cons = models.TextField()
    title=models.TextField(default='')
    employment_status = models.CharField(choices=EMP_STATUS, max_length=50, default='FULLTIME')
    rating = models.IntegerField()
    state=models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return "Review no. " + str(self.id)
