# В google colab добавить: !pip install pyTelegramBotAPI
# Чтобы добавить новое слово — нужно его прописать в массиве DEFINITOINS на 11 строчке
# Важно все новые аббривиатуры в коде писать только с маленьких букв
# Пользователь в телеграм может писать и с большой и с маленькой — код всегда приводит к строчным

from telebot import TeleBot, types

bot = TeleBot(token='Вставьте свой токен сюда', parse_mode='html') # создание бота

# словарь с определениями и аббревиатурами, которые знает бот
# в формате:
# 'ключевая фраза': 'соответствующее ей определение'
DEFINITOINS = {
    'git init': 'сделать из любой папки git папку',
    'git clone': 'склонировать репозиторий на компьюет (git clone ссылка_на_репозиторий)',
    'gut pull': 'спулить обновления',
    'git checkout': 'для переключения между ветками, используй флаг -b чтобы сразу создать и перейти в ветку',
    'git add': 'при добавлении/удалении файлов',
    'git commit': 'сохранить текущие изменения, используй флаг-am "название нового коммита"',
    'git push': 'переносит все изменения, внесенные юзером, в удаленный репозиторий',
    'git status': 'в какой ветке ты находишься',
    'git fetch': 'берет все изменения и сохраняет их локально',
    'git rebase': 'это альтернатива слиянию для задач объединения нескольких веток',
    'git merge': '(слияние) создает новый коммит на основе текущего коммита, применяя изменения других коммитов',
    'git reset': 'отменить изменения(коммит) локально',
    'git log': 'показывает какие файлы ты изменил',
    'git revert': 'отмениться изменения и поделиться с остальными',
    'git rm': 'используется в Git для удаления файлов из индекса и рабочей копии',
    'git mv': 'это всего лишь удобный способ переместить файл, а затем выполнить git add для нового файла и git rm для старого.',
    'git clean': 'используется для удаления мусора из рабочего каталога',
    'git cherry-pick': 'копирование нескольких коммитов на место,где ты находишься'

}

# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    # отправляем ответ на команду '/start'
    bot.send_message(
        chat_id=message.chat.id, # id чата, в который необходимо направить сообщение
        text='Привет! Я шпаргалка по командам гита, помогу тебе расшифровать команду и подскажу, что она делает🤓\nВведи интересующую команду, например, git init', # текст сообщения
    )

# обработчик всех остальных сообщений
@bot.message_handler()
def message_handler(message: types.Message):
    # пробуем найти ключевую фразу в словаре
    definition = DEFINITOINS.get(
        message.text.lower(), # приводим текст сообщения к нижнему регистру
    )
    # если фразы нет в словаре, то переменная definition будет иметь значение None
    # проверяем это условие
    if definition is None:
        # если ключевая фраза не была найдена в словаре
        # отправляем ответ
        bot.send_message(
            chat_id=message.chat.id,
            text='😋 Я пока не знаю такой команды, может спросишь у Гугла?',
        )
        # выходим из функции
        return
    
    # если ключевая фраза была найдена, формируем текст сообщения и отправляем его
    # если перед строкой поставить букву f, то в фигурных скобках {} можно использовать переменные :)
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Определение:\n<code>{definition}</code>',
    )

    bot.send_message(
        chat_id=message.chat.id,
        text=f'Спроси еще!👻',
    )

# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()
