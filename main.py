from pprint import pprint
import re
import csv


def format_number(contacts_list):
    correct_list = list()
    pattern_raw = r'(\+7|8)(\s*)(\(*)(\d{3})([\s\-)]*)(\d{3})([\s\-]*)(\d{2})([\s-]*)(\d{2})(\s*)(\(*)((\w{3})*)(\.*)(\s*)((\w{4})*)(\)*)'
    pattern_correct = r'+7(\4)\6-\8-\10\11\14\15\18'

    for info in contacts_list:
        info_str = ",".join(info)
        correct_info = re.sub(pattern_raw, pattern_correct, info_str)
        info_list = correct_info.split(',')
        correct_list.append(info_list)
    return (correct_list)


def format_name(contacts_list):
    pattern_raw = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
    pattern_correct = r'\1\3\10\4\6\9\7\8'
    correct_list = list()
    for info in contacts_list:
        info_str = ",".join(info)
        correct_info = re.sub(pattern_raw, pattern_correct, info_str)
        info_list = correct_info.split(',')
        correct_list.append(info_list)
    return (correct_list)


def fix_double(contacts_list):
    for i in contacts_list:
        for j in contacts_list:
            if i[0] == j[0] and i[1] == j[1] and i is not j:
                if i[2] == '':
                    i[2] = j[2]
                if i[3] == '':
                    i[3] = j[3]
                if i[4] == '':
                    i[4] = j[4]
                if i[5] == '':
                    i[5] = j[5]
                if i[6] == '':
                    i[6] = j[6]
    correct_list = list()
    for info in contacts_list:
        if info not in correct_list:
            correct_list.append(info)
    return correct_list


if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding="utf8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    print(contacts_list)
    contacts_list = format_number(contacts_list)
    contacts_list = format_name(contacts_list)
    contacts_list = fix_double(contacts_list)


with open("phonebook.csv", "w", encoding="utf8") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(contacts_list)
