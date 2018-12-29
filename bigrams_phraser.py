from gensim.models import Phrases
from gensim.test.utils import datapath

bigrams=Phrases(min_count=3,threshold=6)
with open('C:\\Users\\sreek\\PycharmProjects\\SEC-Edgar-Data\\tokenized_file.txt','r') as tinf,open('C:\\Users\\sreek\\PycharmProjects\\SEC-Edgar-Data\\bi_gram_corpa.txt','a') as toutf:
    for line in tinf:
        bigrams.add_vocab(line)

        toutf.write(''.join(bigrams[line]))
