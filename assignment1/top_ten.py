import sys
import json
import re

def main():
    tweet_file = open(sys.argv[1])
    
    mapState={}
    
    for line in tweet_file:
        if "text" in line:
            dictj = json.loads(line)
            if len(dictj["entities"]["hashtags"])!=0:
                for val in dictj["entities"]["hashtags"]:
                    if val["text"].lower().encode("utf-8") in mapState:
                        mapState[val["text"].lower().encode("utf-8")]+=1
                    else:
                        mapState[val["text"].lower().encode("utf-8")]=1
    
    
    lists = sorted(mapState,key=mapState.__getitem__,reverse=True) 

    i=0
    while (i<10) and (i<len(lists)):
        print lists[i],mapState[lists[i]]
        i+=1
    
            
if __name__ == '__main__':
    main()
