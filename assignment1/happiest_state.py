import sys
import json
import re

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    
    mapState={}
    
    for line in tweet_file:
        if "text" in line:
            dictj = json.loads(line)
            code = ""
            if type(dictj["place"]) is dict:
                if (dictj["place"]["place_type"] == "city") and (dictj["place"]["country_code"] == "US"):
                    code = dictj["place"]["full_name"].encode("utf-8")[-2:]
                    text = dictj["text"].encode("utf-8")
                    text = re.sub(r'[^a-zA-Z0-9]'," ",text)
                    text = re.sub(r'[\t ]+'," ",text)
                    text = re.sub(r'[ ]+',"\t",text)
                    array = text.split('\t')
                    final_score=0
                    for val in array:
                        if val != "":
                            if val in scores:
                                final_score+=scores[val]
                    if code in mapState:
                        mapState[code]+=final_score
                    else:
                        mapState[code]=final_score
    max = -sys.maxint
    finVal = ""
  
    for val in mapState:
        if mapState[val]>max:
            max = mapState[val]                 
            finVal = val
    print val
            
            
if __name__ == '__main__':
    main()
