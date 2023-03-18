import openpyxl


def write_list_emoji(name_table: str, name_file):
    '''Читает таблицу с полным и сокращенным названием, формирует из нее словарь, сохраняет его в файл'''

    book = openpyxl.open(name_table, read_only=True) 
    sheet = book.active

    str_flags = 'emoji: dict = {'
    for row in range(2, sheet.max_row + 1):

        if row:
            if str(sheet[row][1].value).strip() != 'None':

                logo = str(sheet[row][0].value)
                flag = str(sheet[row][1].value)
                flag = ':' + flag.replace('flag: ', '').replace(' ', '_') + ':'
                
                str_flags = str_flags + "'" + logo + "': " + "'" + flag + "', "

    str_flags = str_flags + '}'

    f = open(name_file, 'w', encoding="utf-8")
    f.write(str_flags)
    f.close()



write_list_emoji('flags.xlsx', 'emoji_flags.py')


