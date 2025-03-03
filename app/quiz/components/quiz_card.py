import random

from django_unicorn.components import UnicornView



class QuizCardView(UnicornView):
    question = None
    answers = []

    def mount(self):
        if self.question:
            self.answers = list(self.question.answers.all())
            random.shuffle(self.answers)

