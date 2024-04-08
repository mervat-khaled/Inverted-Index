from sys import stdin
import re

index = {}

for line in stdin:
        word, postings = line.split('\t')

        index.setdefault(word, {})

        for posting in postings.split(','):
                file_id, count = posting.split(':')
                count = int(count)

                index[word].setdefault(file_id, 0)
                index[word][file_id] += count

for word in index:
        postings_list = ["%s:%d" % (doc_id, index[word][file_id])
                         for file_id in index[word]]

        print((word, postings_list))
