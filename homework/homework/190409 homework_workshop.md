190409 homework_workshop

---

```python
class Post(models.Model):
    content = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.[    1     ](settings.AUTH_USER_MODEL, [     2    ]='like_post_set', blank=True)
```

1. Post 모델과 User 모델을 M:N 관계로 설정 하여 좋아요 기능을 구현하려고
  한다. 이때 빨간색 박스에 들어갈 클래스의 이름은 무엇인가?
  - ManyToMany
2. 좋아요 기능을 구현하기 위하여 User모델과 M:N 관계설정을 하려고 한다. 그
  런데 user 칼럼에서 이미 User모델과 관계설정이 되어있기 때문에 이를 구분
  하기 위해 초록색 박스에 들어갈 옵션은 무엇인가?
  - related_name



---

workshop

게시물의 해시태그를 구현하기 위하여 아래와 같이 객체-관계 다이어그램을 작성하였
다. 다이어그램을 바탕으로 models.py 에 Post 모델과 Hashtag 모델을 정의해본다.

```python
# models.py
class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    hashtag = models.ManyToMany(Hashtag, related_name=hash_tag, blank=True)
class Hashtag(models.Model):
    content = models.TextField()
```

