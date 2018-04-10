from mrjob.job import MRJob
#import sys
import os


#os.chdir("/Users/beaubritain/Desktop/lecture_notes/Distributed/wikiproject")


#use output of this in user_dataframe.py
# python by_user.py fixed_subset.txt > output.txt

class subset(MRJob):
    
    def mapper(self, _, line):
        article_id = line.split(" ")[1]
        #article = line.split(" ")[3]
        #user_id = line.split(" ")[6].split("\x1e")[0]
        user_id = line.split(" ")[6]
        user_id = user_id.split("\\u001e")[0]
        yield((user_id + "    " + article_id), 1)

    def reducer(self, key, values):
        yield(key, sum(values))

if __name__ == "__main__":
    subset.run()
    
