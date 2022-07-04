from django.db import models
EMP_STATUS=(
    ("FULLTIME","Full-Time"),
    ("PARTTIME","Part-Time"),
    ("INTERN","Internship"),

)
# Create your models here.
class Review(models.Model):
    company=models.ForeignKey("accounts.User", verbose_name="Company", on_delete=models.CASCADE, related_name='review_company_id')
    reviewer=models.ForeignKey("accounts.User", verbose_name="Reviewer", on_delete=models.CASCADE, related_name="review_employee_id")
    pros=models.TextField()
    cons=models.TextField()
    employment_status=models.CharField(choices=EMP_STATUS, max_length=50)
    rating=models.IntegerField()
    is_published= models.BooleanField(default=False)

    def __str__(self):
        return "Review no. "+self.id
    


