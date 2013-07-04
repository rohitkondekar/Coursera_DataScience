import sys
import json
import re

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    
    for line in tweet_file:
        if "text" in line:
            text = json.loads(line)["text"].encode("utf-8")
            text = re.sub(r'[^a-zA-Z0-9]'," ",text)
            text = re.sub(r'[\t ]+'," ",text)
            text = re.sub(r'[ ]+',"\t",text)
            array = text.split('\t')
            final_score=0
            for val in array:
                if val != "":
                    if val in scores:
                        final_score+=scores[val];
            print final_score
            
if __name__ == '__main__':
    main()
