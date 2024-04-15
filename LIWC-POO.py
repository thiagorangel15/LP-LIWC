import liwc

parse, category_names = liwc.load_token_parser("./LIWC2007_Portugues_win.dic")


class StringReader:
    def __init__(self, filename):
        self.filename = filename
        self.special_characters = {
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
            '\n': ' '
        }

    def read_and_clean(self):
        with open(self.filename, 'r', encoding = "utf-8") as file:
            text = file.read()

            for special_char, normal_char in self.special_characters.items():
                text = text.replace(special_char, normal_char)
            text = text.replace(',', '').replace('.', '').lower()

            tokens = text.split()
        return tokens


class TokenManipulator:
    def __init__(self, tokens):
        self.tokens = tokens

    def count_words(self):
        return len(self.tokens)

    def analyze_sentiment(self):
        swear_count = 0
        anx_count = 0
        posemo_count = 0
        negemo_count = 0

        for token in self.tokens:
            resp = list(parse(token))
            if 'swear' in resp:
                swear_count += 1
            if 'anx' in resp:
                anx_count += 1
            if 'posemo' in resp:
                posemo_count += 1
            if 'negemo' in resp:
                negemo_count += 1

        return {
            'swear_count': swear_count,
            'anx_count': anx_count,
            'posemo_count': posemo_count,
            'negemo_count': negemo_count
        }


class SpecialTokenManipulator(TokenManipulator):
    def __init__(self, tokens):
        super().__init__(tokens)
        self.tokens = tokens


reader = StringReader("arquivo.txt")
tokens = reader.read_and_clean()

print(tokens)

tokens_count = TokenManipulator(tokens).count_words()
tokens_sentiment = TokenManipulator(tokens).analyze_sentiment()

posemo_percent = round((tokens_sentiment['posemo_count']/tokens_count)*100)
negemo_percent = round((tokens_sentiment['negemo_count']/tokens_count)*100)

if posemo_percent > negemo_percent:
    print(f'{tokens_count} palavras. {tokens_sentiment['swear_count']} Palavras ofensivas, {tokens_sentiment['anx_count']} Palavras de ansiedade. tom geral positivo: {posemo_percent}% versus {negemo_percent}% negativo;')
elif negemo_percent > posemo_percent:
    print(f'{tokens_count} palavras. {tokens_sentiment['swear_count']} Palavras ofensivas, {tokens_sentiment['anx_count']} Palavras de ansiedade. tom geral negativo: {negemo_percent}% versus {posemo_percent}% positivo;')
else:
    print(f'{tokens_count} palavras. {tokens_sentiment['swear_count']} Palavras ofensivas, {tokens_sentiment['anx_count']} Palavras de ansiedade. tom geral neutro: {negemo_percent}% negativo versus {posemo_percent}% positivo;')

