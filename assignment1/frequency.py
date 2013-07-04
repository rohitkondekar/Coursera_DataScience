import sys
import json
import re

def main():
    tweet_file = open(sys.argv[1])
    
    terms = {}    
    
    for line in tweet_file:
        if "text" in line:
            text = json.loads(line)["text"].encode("utf-8")
            text = re.sub(r'[^a-zA-Z0-9]'," ",text)
            text = re.sub(r'[\t ]+'," ",text)
            text = re.sub(r'[ ]+',"\t",text)
            array = text.split('\t')
            for val in array:
                if val != "":
                    if val in terms:
                        terms[val]+=1
                    else:
                        terms[val]=1
    
    for val in terms:
        print val,terms[val]                       
                    

if __name__ == '__main__':
    main()
