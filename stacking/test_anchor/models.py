from django.db import models

# Create your models here.


class UserInfo(models.Model):
    user_pubkey = models.CharField(max_length=50)
    stacking_nft_count = models.IntegerField()
    user_signature = models.TextField()
    firth_stacking_data = models.DateTimeField(auto_now_add=True)
    stacking_data_updated_at = models.DateTimeField(auto_now=True)
    nft_image = models.ImageField(upload_to='nfts_img/')
    firth_stacking_duration = models.DurationField()
    is_stacking_active = models.BooleanField(default=False)

    # def __init__(self: _Self, *args, **kwargs) -> None:
    #     super().__init__(*args, **kwargs)
