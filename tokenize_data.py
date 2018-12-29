from nltk import word_tokenize
from nltk import sent_tokenize

with open ('C:\\Users\\sreek\\PycharmProjects\\SEC-Edgar-Data\\output_file.txt') as fin, open('C:\\Users\\sreek\\PycharmProjects\\SEC-Edgar-Data\\tokenized_file.txt','a') as fout:
    for line in fin:
        tokens = word_tokenize(line)
        #print(' '.join(tokens), end='\n', file=fout)
        fout.write(str(tokens))


