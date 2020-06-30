##List of words from sentence
sentence=input()
words = sentence.split()
counts = {}
new_list=[]
for word in words:
    if word not in counts:
        counts[word] = 0
    counts[word] += 1
    if counts[word] < 2:
        new_list.append(word)
print (new_list)
