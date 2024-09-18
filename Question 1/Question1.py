#Question 1
#Group Name: CAS003
#Group Members:
#[Alex Tarrant] - [S255441]
#[Jason Yun] - [S364369]
"""----- Question 1 ----""" 
"""----- Task 1.1 -----"""

writefile = open("HIT137-Assignment-2\Question 1\Combined_text_file.txt", 'w')

#This function opens a file containing text which is provided by the parameter when the funtiton is called, and then copies the text into the open text file.
def text_extract(filename):
    readtext = open(filename,'r')
    sum1=0
    for line in readtext:
        wordlist = line.split()
        for word in wordlist:
            writefile.write(word + " ")

#The function is used on all of the CSV files 
text_extract("CSV1.csv")  
text_extract("CSV2.csv")    
text_extract("CSV3.csv")    
text_extract("CSV4.csv")      

writefile.close        
print ("Complete")

"""----- Task 1.2 -----"""
#Ensure the following commands are exectued in the command line or terminal to install the libraries
"""
pip install scispacy
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_core_sci_sm-0.5.4.tar.gz
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_ner_bc5cdr_md-0.5.4.tar.gz
pip install transformers
git clone https://github.com/dmis-lab/biobert.git
cd biobert; pip install -r requirements.txt
"""

"""----- Task 1.3.1 -----"""
#This code opens the combined text file and separates the individual words, every word is added to a the new dictionary and counted.
readfile = open("HIT137-Assignment-2\Question 1\Combined_text_file.txt", 'r')
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
                worddict[word] = 1

#The dictionary is sorted with words with most common words to least common words.                
sorteddict = dict(sorted(worddict.items(), key=lambda item: item[1], reverse = True))
top30words = {k: sorteddict[k] for k in list(sorteddict)[:30]}

#The top 30 most common words are written into a CSV file.
writefile = open("HIT137-Assignment-2\Question 1\Top_30_Words.csv", 'w')
writefile.write("The top 30 most common words in the CSV files are: \n")
for line in top30words:
        wordlist = line.split()
        for word in wordlist:
            writefile.write(word + ":" + str(top30words.get(word)) + " \n")

writefile.close        
print ("Complete")

"""----- Task 1.3.2 ----"""
#Our Team was not able complete this task of the assignment.