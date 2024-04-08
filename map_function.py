import re
import os
import nltk
from nltk.corpus import stopwords
import pathlib

def mapper(path):
    stopwords = nltk.corpus.stopwords.words('english')
    for txt_file in pathlib.Path(path).glob('*.txt'):
        with open(txt_file,'r') as file:
            _,file_id=os.path.split(txt_file)
            file=file.read()
            words = re.findall(r'\w+', file.lower())
            for word in words:
                if word not in stopwords:
                    print("%s\t%s:1" % (word, file_id))