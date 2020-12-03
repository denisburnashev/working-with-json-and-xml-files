def counting_top_words_in_xml(file_name):
    from collections import Counter
    import xml.etree.ElementTree as ET
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(file_name, parser)
    root = tree.getroot()
    news_xml = root.findall('channel/item')

    for news in news_xml:
        news_inf = news.find('description').text
        news_list = news_inf.lower().split(' ')
        news_list.sort()

    sorted_list = []

    for words in news_list:
        if len(words) >= 6:
            sorted_list.append(words)
            sorted_words = Counter(sorted_list).most_common(10)
    print(sorted_words)

    sorted_words = {}

    for words in sorted_list:
        if words in sorted_words:
            sorted_words[words] += 1
        else:
            sorted_words[words] = 1
    inverse = [(value, key) for key, value in sorted_words.items()]
    reverse_inverse = sorted(inverse, reverse=True)
    sorted_list_1 = []
    for word in reverse_inverse[0:10]:
        qwe = (word[1], word[0])
        sorted_list_1.append(qwe)
    print(sorted_list_1)

counting_top_words_in_xml('newsafr.xml')
