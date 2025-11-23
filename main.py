from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Простые рекомендации фильмов по настроению
movie_recommendations = {
    "позитивное": [
        "«Назад в будущее» - отличный приключенческий фильм, который поднимет настроение еще выше!",
        "«Одноклассники» - веселая комедия про школьные годы",
        "«Тайна Коко» - красивая и добрая анимация про семью и музыку"
    ],
    "негативное": [
        "«Побег из Шоушенка» - вдохновляющая история о надежде и свободе",
        "«Области тьмы» - интересный триллер, который отвлечет от грустных мыслей",
        "«1+1» - трогательная комедия-драма про дружбу"
    ],
    "нейтральное": [
        "«Начало» - захватывающий научно-фантастический триллер",
        "«Король говорит!» - историческая драма с прекрасной актерской игрой",
        "«Джентльмены» - стильный криминальный фильм с юмором"
    ]
}

def analyze_mood_simple(text):
    """Простой анализ настроения по ключевым словам"""
    text = text.lower()
    
    positive_words = ['хорош', 'отличн', 'прекрасн', 'рад', 'счастлив', 'весел', 'класс', 'супер']
    negative_words = ['плох', 'ужасн', 'грустн', 'печаль', 'злой', 'раздража', 'скучн']
    
    positive_count = sum(1 for word in positive_words if word in text)
    negative_count = sum(1 for word in negative_words if word in text)
    
    if positive_count > negative_count:
        return "позитивное"
    elif negative_count > positive_count:
        return "негативное"
    else:
        return "нейтральное"

def generate_recommendation_simple(mood):
    """Простая генерация рекомендации"""
    recommendations = movie_recommendations.get(mood, movie_recommendations["нейтральное"])
    return random.choice(recommendations)

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendation = ""
    user_text = ""
    ai_result = ""

    if request.method == "POST":
        user_text = request.form.get("message", "").strip()
        if not user_text:
            recommendation = "Ты ничего не ввёл!"
        else:
            # Простой анализ настроения
            mood = analyze_mood_simple(user_text)
            
            if mood == "позитивное":
                recommendation = "Позитивное настроение!"
            elif mood == "негативное":
                recommendation = "Негативное настроение."
            else:
                recommendation = "Нейтральное настроение."
            
            # Генерация рекомендации
            ai_text = generate_recommendation_simple(mood)
            ai_result = f"Настроение: {recommendation}. Рекомендация: {ai_text}"

    return render_template('index.html',
                           recommendation=recommendation,
                           user_text=user_text,
                           ai_result=ai_result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)