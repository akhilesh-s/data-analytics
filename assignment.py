import re

#string of question words
str = ["how", "what", "when", "que", "who", "why", "whose", "which", "where"]

with open('data.txt','r') as firstfile, open('data2.txt','a') as secondfile:
    for line in firstfile:
        count=0
        for s in str:
            count=re.findall('\\b' + s + '\\b', line, flags=re.IGNORECASE)
            if len(count) > 0:
                break
        if count:
            secondfile.writelines(line + "Yes" + "\n")
        else:
            secondfile.writelines(line + "No" + "\n")

