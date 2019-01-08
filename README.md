
# 10k_embeddings

I made a couple of modifications to a forked code on github to download multiple files parallely and BeautifuSoup to clean HTML tags from files. Merged files downloaded  into a single text and pre processed data to remove numbers , punctuations and any non alpha numeric characters. Used Gensim library to create bi-grams . Could extend that corpus to include tri-grams. Used Keras with tensorflow backend to create word vector with demensions 200 , window size 5 and a threshold for words to appear in the corpus is also 5. 

Built another word embedding using gensim and the command with params is

"python -m gensim.scripts.word2vec_standalone -train <<your_file_name>> -output pwc.10kq.200d.bin  -size 200 -sample 1e-4 -binary 1 -cbow 0"
