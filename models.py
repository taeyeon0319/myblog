from django.db improt models

class Post(models.Model):
    title = models.CharField(max_length=50, null=False)
    content = models.TextField()
    view_count = models.PositiveSmallIntegerField(defalut = 0)
    created_at = models.DataTimeField(auto_now_add = True)
    updated_at = models.DataTimeField(auto_now = True)

    podol2= models.Manager()