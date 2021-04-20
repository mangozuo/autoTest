from django.db import models
from django.contrib.auth.models import User

# Create your models here.

Project_Type_Choice = (
    ("Web", "Web"),
    ("App", "App")
)

HTTP_CHOICE = (
    ('HTTP', 'HTTP'),
    ('HTTPS', 'HTTPS')
)

REQUEST_TYPE_CHOICE = (
    ('POST', 'POST'),
    ('GET', 'GET'),
    ('PUT', 'PUT'),
    ('DELETE', 'DELETE')
)

REQUEST_PARAMETER_TYPE_CHOICE = (
    ('form-data', '表单(form-data)'),
    ('Restful', 'Restful')
)

PARAMETER_TYPE_CHOICE = (
    ('text', 'text'),
    ('file', 'file')
)

RESPONSE_TYPE_CHOICE = (
    ('Int', 'Int'),
    ('String', 'String'),
    ('Re', 'Re(正则匹配)')
)

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True, verbose_name="项目名称")
    version = models.CharField(max_length=64, verbose_name="版本信息")
    type = models.CharField(max_length=16, choices=Project_Type_Choice, default="Web",
                            verbose_name="项目类型")
    status = models.BooleanField(default=True, verbose_name="状态")
    description = models.CharField(max_length=256, verbose_name="项目描述")
    createTime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    lastUpdateTime = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    createUser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                   verbose_name="创建人")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "项目"
        verbose_name_plural = "项目信息"
