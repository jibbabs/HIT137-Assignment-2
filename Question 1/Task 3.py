"""from transformers import AutoTokenizer, AutoModelForMaskedLM

tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.2")
model = AutoModelForMaskedLM.from_pretrained("dmis-lab/biobert-base-cased-v1.2")"""
"""
readfile = open("Combined_text_file.txt", 'r')
sum1=0
worddict = {}
for line in readfile:
    wordlist = line.split()
    for word in wordlist:
        word = word.strip()
        word = word.lower() 
        seperatewords = word.split(" ") 
        for word in seperatewords:
            if word in worddict:
                worddict[word] = worddict[word] + 1
            else:
                worddict[word] = 1"""
   
listtemp = {"1":"4", "2":"5", "3":"8", "4":"2"} 
printlist = []               
listwords = int(max(listtemp.values()))
for listtemp.values <= listwords -2:
    printlist.append(items)

print(printlist)

print(listwords)
#for key in list(worddict.keys()): 
 #   print(key, ":", worddict[key]) 