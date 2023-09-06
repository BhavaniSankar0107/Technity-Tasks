import os
import telebot
import requests
import json
import csv

# TODO: 1.1 Get your environment variables
api_key = 'e7eb5970'
bot_token = '6376341100:AAEuVncwLCCLvWhjN8lvgXaCnWiddS-ReEg'

bot = telebot.TeleBot(bot_token)
botRunning = False

@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')

@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')

@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use "/movie MOVIE_NAME" command to get the details of a particular movie. For example: "/movie The Shawshank Redemption"\n\n2.0 You can use "/export" command to export all the movie data in CSV format.\n\n3.0 You can use "/stop" or the command "/bye" to stop the bot.')

@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    bot.reply_to(message, 'Getting movie info...')
    movie_name = message.text[7:]  # Extract the movie name from the command
    movie_data = get_movie_info(movie_name)
    if movie_data:
        movie_info = f"Title: {movie_data['Title']}\nYear: {movie_data['Year']}\nPlot: {movie_data['Plot']}"
        bot.send_message(message.chat.id, movie_info)
        save_movie_to_csv(movie_data)
    else:
        bot.send_message(message.chat.id, "Movie not found or an error occurred.")

@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating file...')
    send_csv_file(message.chat.id)

@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand ' + '\N{confused face}')

def get_movie_info(movie_name):
    api_url = f"http://www.omdbapi.com/?t={movie_name}&apikey={api_key}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None

def save_movie_to_csv(movie_data):
    with open('movie_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Year', 'Plot'])  # Write header row
        writer.writerow([movie_data['Title'], movie_data['Year'], movie_data['Plot']])  # Write movie data

def send_csv_file(chat_id):
    with open('movie_data.csv', 'rb') as file:
        bot.send_document(chat_id, file)

bot.infinity_polling()
