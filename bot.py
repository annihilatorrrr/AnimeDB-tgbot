import telebot,search

bot = telebot.TeleBot("1153023482:AAHqxLOLkXs6XdDb9-tQ-hOANeJVoHiYFIw")

help_str = """
Here is the list of commands
/anime - To search a anime by name
/manga - To search a manga by name
/help - Show commands
"""

stype = {
  'anime' : '🎬 Anime',
  'manga' : '📃 Manga'
  }

@bot.message_handler(commands=['start'])
def send_welcome(m):
	bot.reply_to(m, "Welcome to @AnimeDB_Bot")

@bot.message_handler(commands=['help'])
def send_help(m):
	bot.reply_to(m, help_str)

@bot.message_handler(commands=['anime','manga'])
def search_xxx(m):
  s_type = telebot.util.extract_command(m.text)
  key = telebot.util.extract_arguments(m.text)
  
  if not key:
    bot.reply_to(m,f"<b>Example : </b>`/{s_type} Naruto`",parse_mode='HTML')
  else:
    print(" Searching for",key)
    result = search.search_anime(s_type,key)
    if result != 0:
      print(f" Result Found for {key}")
      poster = result["attributes"]["posterImage"]["large"]
      synopsis = "<b>📖 Synopsis : </b> "+result['attributes']['synopsis']
      caption = (f"<b>{stype[s_type]} : </b>{result['attributes']['canonicalTitle']}\n"
      f"<b>⭐ Average Rating : </b>{result['attributes']['averageRating']}\n"
      f"<b>🔰 Status : </b>{result['attributes']['status']}\n"
      f"<b>👤 Age Rating : </b>{result['attributes']['ageRating']} ({result['attributes']['ageRatingGuide']})\n")
      bot.send_photo(m.chat.id,poster,caption,parse_mode='HTML')
      bot.send_message(m.chat.id,synopsis,parse_mode='HTML')
    else:
      bot.reply_to(m,f"No {s_type} found ☹️")

bot.polling()