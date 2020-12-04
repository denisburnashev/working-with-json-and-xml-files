from collections import Counter
import json

all_words = []
sorted_list = []


def opening_and_reading_xml(file_name):
    import xml.etree.ElementTree as ET
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(file_name, parser)
    root = tree.getroot()
    news_xml = root.findall('channel/item')
    all_words.clear()
    for news in news_xml:
        news_inf = news.find('description').text
        news_list = news_inf.lower().split(' ')
        for word in news_list:
            all_words.append(word)


def opening_and_reading_json(file_name):
    with open(file_name, encoding='utf-8') as sorting_words:
        json_data = json.load(sorting_words)
        all_news = json_data['rss']['channel']['items']
        all_words.clear()
        for description in all_news:
            words = description['description'].split(' ')
            for word in words:
                all_words.append(word)


#Filtering by numbers of letters in a word
def fliter(user_input):
  for word in all_words:
    if len(word) >= user_input:
      sorted_list.append(word)

#Top often words in news
def top_words(user_input):
    sorted_words = Counter(sorted_list).most_common(user_input)
    print(sorted_words)
    sorted_list.clear()


def main():
    while True:
        user_input = input('Введите вашу команду: \n x для получения данных из xml файла \n j для получения данных из json файла\n exit для выхода из программы\n')
        if user_input == 'x':
            opening_and_reading_xml('newsafr.xml')
            user_input = int(input('Введите число букв в слове для фильтрации списка слов:'))
            fliter(user_input)
            user_input = input('Если вы хотите посмотреть отфильтрованный список введите list, если хотите увидеть топ слов введите top:\n')
            if user_input == 'list':
                print(sorted_list)
                sorted_list.clear()
            elif user_input == 'top':
                user_input = int(input('Введите число топ скольки слов вы хотите увидеть:\n'))
                top_words(user_input)
        elif user_input == 'j':
            opening_and_reading_json('newsafr.json')
            user_input = int(input('Введите число букв в слове для фильтрации списка слов:'))
            fliter(user_input)
            user_input = input('Если вы хотите посмотреть отфильтрованный список введите list, если хотите увидеть топ слов введите top:\n')
            if user_input == 'list':
                print(sorted_list)
                sorted_list.clear()
            elif user_input == 'top':
                user_input = int(input('Введите число топ скольки слов вы хотите увидеть:\n'))
                top_words(user_input)
        elif user_input == 'exit':
            break

main()
