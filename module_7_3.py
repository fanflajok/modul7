class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, 'r', encoding = 'utf-8') as file:
                N = file.read().lower()
                for j in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    N = N.replace(j, ' ')
                all_words[i] = N.split()
        return all_words
    def find(self, word):
        found_word = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                found_word[name] = words.index(word.lower())+1
        return found_word
    def count(self, word):
        sow = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                sow[name] = words.count(word.lower())
        return sow




f1 = WordsFinder('products.txt', 'test.txt', 'для_дз.txt')
print(f1.get_all_words())
print(f1.find("Vegetables"))
print(f1.count('tExt'))