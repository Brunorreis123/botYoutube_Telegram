import telebot
import subprocess

bot_token = 'insira seu token'
bot = telebot.TeleBot(bot_token)

# Remova o webhook antes de iniciar o polling
bot.delete_webhook()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Olá! Envie-me o link do vídeo do YouTube que você deseja fazer o download.')


@bot.message_handler(func=lambda message: True)
def download_video(message):
    video_url = message.text
    video_filename = 'video.mp4'
    subprocess.call(['youtube-dl', '-o', video_filename, video_url])
    video_file = open(video_filename, 'rb')
    bot.send_video(message.chat.id, video_file)
    video_file.close()


bot.polling()
