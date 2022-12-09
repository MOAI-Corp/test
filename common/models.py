from django.db import models


class CommonModel(models.Model):

    """Common Model Definition"""

    """데이터베이스에 저장하지 않고, 재사용하기 위한 app임
    created_at과 updated_at이 여러 클래스에서 반복사용되기 때문에 따로 common이라는 반복사용할 app을 생성
    class Meta를 통해서 데이터베이스에 저장하지 않게 만듬"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Create your models here.
