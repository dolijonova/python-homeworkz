print("Enter your paragraph or text")
txtfile=input()
cleaned_text=txtfile.lower().replace('.','')\
.replace(',','').replace('\n','').split()
# made a list which is easier to compare
wordcount={}
for word in cleaned_text:
    if word in wordcount:
        wordcount[word]+=1
    else:
        wordcount[word]=1

sortedwordcount=sorted(wordcount.items()) 
top5= sortedwordcount[:5]

print("Top 5 most common words:")
for word, count in top5:
    print(f"{word}: {count}")

with open("word_count_report.txt", "w") as file:
    file.write("Top 5 most common words:\n")
    for word, count in top5:
        file.write(f"{word}: {count}\n")

print("Report saved to 'word_count_report.txt'.")

    
 

