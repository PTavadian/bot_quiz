from random import randint 




def filter_sort(get_words: list[tuple[str | None]], emoji: tuple[str | None]) -> list[list[str | None]]:
    '''Сортирует слова по типу'''

    #https://unicode.org/emoji/charts/full-emoji-list.html

    emoji = list(emoji)
    
    for i, e in enumerate(emoji):
        if not emoji[i]:
            emoji[i] = ''

    words_with_type: dict[list[list[str]]] = dict()
    len_words_with_type = dict()

    words: list[list[str]] = list()
    for i, row in enumerate(get_words):
        words.append([])

        for c, column in enumerate(row):
            if c > 3:
                break
            words[i].append(emoji[c] + column if column else '') 

        for c, column in enumerate(row):
            if column and c > 3:
                if not column in words_with_type:
                    words_with_type[column] = [words[i]]
                else:
                    words_with_type[column].append(words[i])

                len_words_with_type[column] = len(words_with_type[column])

            elif c > 3:
                if not 'NULL' in words_with_type:
                    words_with_type['NULL'] = [words[i]]
                else:
                    words_with_type['NULL'].append(words[i])

                len_words_with_type['NULL'] = len(words_with_type['NULL'])


    list_type: list[str] = list() #список из ключей с учетом соотношения их количества
    for o in words_with_type:
        for u in range(len_words_with_type[o]):
            list_type.append(o)


    some_type = list_type[randint(0, len(list_type) - 1)]
    res = set()
    while len(res) < 4: 
        res.add(tuple(words_with_type[some_type][randint(0, len(words_with_type[some_type]) - 1)]))
        if len(res) == len(words_with_type[some_type]):
            break


    send_words = []
    for row in res:
        send_words.append(list(row))

    return send_words







def filter(result: list[tuple[str | None]], emoji: tuple[str | None]) -> list[list[str]]:

    #https://unicode.org/emoji/charts/full-emoji-list.html

    emoji = list(emoji)
    
    for i, e in enumerate(emoji):
        if not emoji[i]:
            emoji[i] = ''


    res = set()
    while len(res) < 4: 
        res.add(result[randint(0, len(result) - 1)])

    words: list[list[str]] = list()
    for i, row in enumerate(res):
        words.append([])
        for c, column in enumerate(row):

            if c > 3:
                break
            if column:
                words[i].append(emoji[c] + column)

    return words









