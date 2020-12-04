from collections import Counter
import json

sorted_list = []


def counting_top_words_in_xml(file_name, user_input):
    import xml.etree.ElementTree as ET
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(file_name, parser)
    root = tree.getroot()
    news_xml = root.findall('channel/item')
    for news in news_xml:
        news_inf = news.find('description').text
        news_list = news_inf.lower().split(' ')
    for words in news_list:
        if len(words) >= user_input:
            sorted_list.append(words)
    user_input = input('Если вы хотите посмотреть отфильтрованный список введите list, если хотите увидеть топ слов введите top:\n')
    if user_input == 'list':
        print(sorted_list)
        sorted_list.clear()
    elif user_input == 'top':
        top_words()


def counting_top_words_in_json(file_name, user_input):
    with open(file_name, encoding='utf-8') as sorting_words:
        json_data = json.load(sorting_words)
        all_news = json_data['rss']['channel']['items']
        for description in all_news:
            words = description['description'].split(' ')
        for word in words:
            if len(word) >= user_input:
                sorted_list.append(word)
        user_input = input('Если вы хотите посмотреть отфильтрованный список введите list, если хотите увидеть топ слов введите top:\n')
        if user_input == 'list':
            print(sorted_list)
            sorted_list.clear()
        elif user_input == 'top':
            top_words()


def top_words():
    user_input = input('Введите число топ скольки слов вы хотите увидеть:\n')
    sorted_words = Counter(sorted_list).most_common(int(user_input))
    print(sorted_words)
    sorted_list.clear()


def main():
    while True:
        user_input = input('Введите вашу команду: \n x для получения данных из xml файла \n j для получения данных из json файла\n exit для выхода из программы\n')
        if user_input == 'x':
            user_input = int(input('Введите число букв в слове для фильтрации списка слов:'))
            counting_top_words_in_xml('newsafr.xml', user_input)
        elif user_input == 'j':
            user_input = int(input('Введите число букв в слове для фильтрации списка слов:'))
            counting_top_words_in_json('newsafr.json', user_input)

        elif user_input == 'exit':
            break

main()
