import telebot
from data import indices, X, data
from sklearn.metrics.pairwise import laplacian_kernel
from fuzzywuzzy import fuzz
import sys

sim = laplacian_kernel(X, X)

class MovieRecommender:
    def __init__(self, data, indices, sim):
        self.data = data
        self.indices = indices
        self.sim = sim

    def get_recommendation(self, title):
        possible_matches = []
        try:
            idx = self.indices[title]
            sim_scores = enumerate(self.sim[idx])
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            sim_scores = sim_scores[1:8]
            sim_index = [i[0] for i in sim_scores]
            recommendations = [self.data["заголовок"].iloc[i] for i in sim_index]
        except KeyError:
            recommendations = []
            for movie_title in self.indices.index:
                ratio = fuzz.partial_ratio(title.lower(), movie_title.lower())
                if ratio >= 85:
                    possible_matches.append(movie_title)

            if possible_matches:
                recommendations = ["Возможно, вы имели в виду:"] + [match for match in possible_matches if match != "O"]
            else:
                recommendations = ["Такого фильма у нас нет ( ◡‿◡ *)"]

        return recommendations
API_TOKEN='ТОКЕН'
bot = telebot.TeleBot(API_TOKEN)
recommender = MovieRecommender(data, indices, sim)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Напишите название фильма, а мы найдем похожий ╰(▔∀▔)╯")

@bot.message_handler(func=lambda message: True)
def get_recommendation(message):
    title = message.text
    if len(title) < 2:
        bot.send_message(message.chat.id, "Пожалуйста, введите более длинное название фильма.")
    else:
        recommendations = recommender.get_recommendation(title)
        response = "\n".join(recommendations)
        bot.send_message(message.chat.id, response)
bot.infinity_polling()
