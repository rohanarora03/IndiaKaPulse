import nltk
import string
import collections
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
postags = ['NN', 'NNS', 'NNP', 'NNPS']
adj = ['JJ', 'JJR', 'JJS']
l = []
ll = []


class relevant(object):

    def find_relevant(self):

        stop_words = set(stopwords.words('english'))
        stop_words.remove('no')
        stop_words.remove('nor')
        stop_words.remove('not')

        f = open('scrape_data_final.txt', 'rb+')
        my_dict = eval(f.read())

        for line in my_dict:
            tokens = word_tokenize(line)
            tokens = [word.lower() for word in tokens if len(word) > 1]
            words_postags = nltk.pos_tag(tokens)
            table = str.maketrans('', '', string.punctuation)
            tokens = [w.translate(table) for w in tokens]
            tokens = [word for word in tokens if word.isalpha()]
            tokens = [w for w in tokens if w not in stop_words]
            for word_postag in words_postags:
                if word_postag[0] in tokens:
                    ll.append(word_postag)

        tags = []
        words = []
        for i in ll:
            tags.append(i[1])
            words.append(i[0])

        most_common = collections.Counter(words).most_common()  

        freq_sum_word = 0  
        total_num_words = 0  
        freq_sum_word_chk = 0  

        for freq_dist in most_common:
            freq_sum_word = freq_sum_word + freq_dist[1]

        for freq_dist in most_common:
            total_num_words = total_num_words + 1
            freq_sum_word_chk = freq_sum_word_chk + freq_dist[1]
            if freq_sum_word_chk > (freq_sum_word / 2):
                break

        most_common_final = collections.Counter(words).most_common(total_num_words)
        s = 0
        for i in most_common_final:
            s = s + i[1]

        lis = []
        for j in most_common_final:
            prt = j[1] / s
            lis.append((j[0], prt * 100))

        print("Keyword based result:-")
        print(lis)
        print(most_common_final)
