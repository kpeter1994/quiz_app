import pandas as pd

from django.shortcuts import render, redirect
from .models import Question, Answer, Score, GameUser
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, LoginForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):

    return render(request, 'index.html')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})

def game(request):
    questions = Question.objects.all()
    return render(request,'game.html',{'questions': questions} )

def ranking(request):
    scores = Score.objects.all().order_by("-score")

    df = pd.DataFrame(list(scores.values("user__username", "score")))

    if not df.empty:
        stats = df.groupby("user__username")["score"].agg(
            avg_score="mean",
            max_score="max",
            std_score="std",
            count="count"
        ).reset_index()

        stats["std_score"].fillna(0, inplace=True)

        stats = stats.sort_values("avg_score", ascending=False).head(10)
    else:
        stats = pd.DataFrame(columns=["user__username", "avg_score", "max_score", "std_score", "count"])

    return render(request, 'ranking.html', {"scores": scores, "stats": stats.to_dict(orient="records")})


@csrf_exempt
def quiz_submit(request):
    score_message = []
    score = 0

    if request.method == "POST":

        for key, value_list in request.POST.lists():
            if key == "csrfmiddlewaretoken":
                continue
            question = Question.objects.get(id=int(key))

            if question.q_type in ["numerical"]:
                correct_answer = question.answers.filter(is_correct=True)
                if int(correct_answer[0].text) == int(value_list[0]):
                    score += question.difficulty
                    score_message.append({
                        "question": question.text,
                        "answer": correct_answer[0].text,
                        "correct": True}
                    )
                else:
                    score_message.append({
                        "question": question.text,
                        "answer": correct_answer[0].text,
                        "correct": False }
                    )

            if question.q_type not in ["numerical"]:
                correct_answers = question.answers.filter(is_correct=True)

                for value in value_list:
                    for correct_answer in correct_answers:
                        if correct_answer.id == int(value):
                            score += question.difficulty
                            score_message.append({
                                "question": question.text,
                                "answer": correct_answer.text,
                                "correct": True}
                            )
                        else:
                            score_message.append({
                                "question": question.text,
                                "answer": correct_answer.text,
                                "correct": False }
                            )
        score_data = Score(user=request.user, score=score)
        score_data.save()

        response_data = {
            "message": "Adatok sikeresen beérkeztek!",
            "submitted_data": dict(request.POST),
            "score_message": score_message,
            "score": score
        }
        return JsonResponse(response_data)

    return JsonResponse({"error": "Hibás kérés!"}, status=400)
