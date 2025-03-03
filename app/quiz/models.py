from django.db import models
from django.conf import settings
from django.contrib.auth.hashers import make_password


class Question(models.Model):
    QUESTION_TYPES = [
        ('scq', 'Szimpla válasz'),
        ('mcq', 'Többszörös válasz'),
        ('true_false', 'Igaz/Hamis'),
        ('short_answer', 'Rövid válasz'),
        ('numerical', 'Számmal megadott válasz'),
    ]

    # Lehetséges kategóriák
    CATEGORIES = [
        ('science', 'Tudomány'),
        ('history', 'Történelem'),
        ('geography', 'Földrajz'),
        ('math', 'Matematika'),
        ('literature', 'Irodalom'),
        ('art', 'Művészet'),
        ('music', 'Zene'),
        ('sports', 'Sport'),
        ('technology', 'Technológia'),
        ('health', 'Egészség'),
        ('languages', 'Nyelvek'),
        ('movies', 'Filmek'),
        ('gaming', 'Videójátékok'),
        ('politics', 'Politika'),
        ('economy', 'Gazdaság'),
        ('environment', 'Környezetvédelem'),
        ('psychology', 'Pszichológia'),
        ('philosophy', 'Filozófia'),
        ('mythology', 'Mitológia'),
        ('space', 'Űrkutatás'),
    ]

    text = models.CharField(max_length=255)
    q_type = models.CharField(max_length=255, choices=QUESTION_TYPES)
    difficulty = models.IntegerField()
    category = models.CharField(max_length=255, choices=CATEGORIES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.text

class Score(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.score}"

class GameUser(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.password.startswith("pbkdf2_sha256$"):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name