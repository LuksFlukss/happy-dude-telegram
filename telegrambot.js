const TelegramBot = require('node-telegram-bot-api');

const token = '6229406234:AAFP_uDSOVKc7Zjkp9wFBEwBZYHhm6yupUw';

const bot = new TelegramBot(token, { polling: true });

bot.on('message', (msg) => {
    const chatId = msg.chat.id;
  
    bot.sendMessage(chatId, 'Please choose an option:', {
      reply_markup: {
        keyboard: [
          [{ text: 'Option 1' }, { text: 'Option 2' }],
          [{ text: 'Option 3' }],
        ],
        resize_keyboard: true,
        one_time_keyboard: true,
      },
    });
  });  