import telebot
from telebot import types

# Set up your Telegram bot API token here
bot = telebot.TeleBot("6229406234:AAFP_uDSOVKc7Zjkp9wFBEwBZYHhm6yupUw")

# This function will handle the "/start" command
@bot.message_handler(commands=['start'])
def start_handler(message):
    # Create the navigation menu with 7 buttons, in rows of 2/3
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    menu.add(types.KeyboardButton("go"), types.KeyboardButton("go1"))
    menu.add(types.KeyboardButton("go2"), types.KeyboardButton("go3"))
    menu.add(types.KeyboardButton("go4"), types.KeyboardButton("go5"))
    menu.add(types.KeyboardButton("go6"))

    # Send the "Hello!" message and the navigation menu to the user
    bot.send_message(message.chat.id, "Hello!", reply_markup=menu)
    print('Hello!')

# This function will handle the "go" category
@bot.message_handler(func=lambda message: message.text == 'go')
def go_handler(message):
    # Send the "go" message to the user
    bot.send_message(message.chat.id, "go")

    # Create the navigation menu with the "back to main menu" button
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    menu.add(types.KeyboardButton("back to main menu"))

    # Send the navigation menu to the user
    bot.send_message(message.chat.id, "Choose an option:", reply_markup=menu)

# This function will handle the "back to main menu" button
@bot.message_handler(func=lambda message: message.text == 'back to main menu')
def back_handler(message):
    # Create the navigation menu with 7 buttons, in rows of 2/3
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    menu.add(types.KeyboardButton("go"), types.KeyboardButton("go1"))
    menu.add(types.KeyboardButton("go2"), types.KeyboardButton("go3"))
    menu.add(types.KeyboardButton("go4"), types.KeyboardButton("go5"))
    menu.add(types.KeyboardButton("go6"))

    # Send the navigation menu to the user
    bot.send_message(message.chat.id, "Choose an option:", reply_markup=menu)

# Start the bot
bot.polling()