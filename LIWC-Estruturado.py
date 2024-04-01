import liwc
parse, category_names = liwc.load_token_parser("./LIWC2007_Portugues_win.dic")

archive = open("arquivo.txt","r", encoding = "utf-8")


specials_caracters = {
    'á': 'a',
    'à': 'a',
    'â': 'a',
    'ã': 'a',
    'é': 'e',
    'ê': 'e',
    'í': 'i',
    'ó': 'o',
    'ô': 'o',
    'õ': 'o',
    'ú': 'u',
    'ç': 'c',
    'Á': 'A',
    'À': 'A',
    'Â': 'A',
    'Ã': 'A',
    'É': 'E',
    'Ê': 'E',
    'Í': 'I',
    'Ó': 'O',
    'Ô': 'O',
    'Õ': 'O',
    'Ú': 'U',
    'Ç': 'C',
    '\n':' '
}

text = archive.read()

text_list = list(text)
text_list_with_no_specials = list()

for letter in text_list:
    if letter in specials_caracters:
        text_list_with_no_specials.append(specials_caracters[letter])
    else:
        text_list_with_no_specials.append(letter)


treated_text_list = list()

for letter in text_list_with_no_specials:

    if 65 <= ord(letter) <= 90:
        treated_text_list.append(chr(ord(letter)+32))

    elif 97 <= ord(letter) <= 122 or ord(letter) == 32:
        treated_text_list.append(letter)

treated_text = ''.join(treated_text_list)
# print(treated_text)

tokens = treated_text.split()
# print(tokens)

swear_counter = 0
anx_counter = 0
posemo_counter = 0
negemo_counter = 0
word_counter = len(tokens)


#print(word_counter)

for token in tokens:
    resp = list(parse(token))
    if 'swear' in resp:
        swear_counter += 1
    if 'anx' in resp:
        anx_counter += 1
    if 'posemo' in resp:
        posemo_counter += 1
    if 'negemo' in resp:
        negemo_counter += 1



posemo_percent = round((posemo_counter/word_counter)*100)
negemo_percent = round((negemo_counter/word_counter)*100)

if posemo_percent > negemo_percent:
    print(f'{word_counter} palavras. {swear_counter} Palavras ofensivas, {anx_counter} Palavras de ansiedade. tom geral positivo: {posemo_percent}% versus {negemo_percent}% negativo;')
elif negemo_percent > posemo_percent:
    print(f'{word_counter} palavras. {swear_counter} Palavras ofensivas, {anx_counter} Palavras de ansiedade. tom geral negativo: {negemo_percent}% versus {posemo_percent}% positivo;')
else:
    print(f'{word_counter} palavras. {swear_counter} Palavras ofensivas, {anx_counter} Palavras de ansiedade. tom geral neutro: {negemo_percent}% negativo versus {posemo_percent}% positivo;')
