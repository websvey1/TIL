190410 homework_workshop

---

1. Django에서 validator는 일부 조건이 충족되지 않으면 특정 에러를 발생시켜
  값이 정확하게 들어왔는지 확인한다. 이때 발생 시키는 에러를 작성하시오.

  - ```
    ValidationError
    ```

2. 공식문서를 통해서 장고가 가지고 있는 Built-in validator를 찾아서 3개 이상
  작성하시오.

  - [`RegexValidator`](https://docs.djangoproject.com/en/2.2/ref/validators/#regexvalidator)
  - [`EmailValidator`](https://docs.djangoproject.com/en/2.2/ref/validators/#emailvalidator)
  - [`URLValidator`](https://docs.djangoproject.com/en/2.2/ref/validators/#urlvalidator)

---





![1556160781321](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1556160781321.png)

```python
#model.py
class Person(models.Model):
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100,
                    validators=[EmailValidator(message="이메일 형식에 맞지 않습니다")])
    age = models.IntegerField(validators =[MinValueValidator(19, message="미성년자는 노노")])
```

```python
#admin.py
class PersonAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'email', 'age']
admin.site.register(Person, PersonAdmin)
```

