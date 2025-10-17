with open('codingal.txt','w') as file:
    file.write("Im Arham im 9 years old.")
    file.close()
with open('codingal.txt','r') as file:
    data=file.readlines()
    print("The WORDS IN THE FILE ARE: ")
    for line in data:
        word=line.split()
        print(word)
    file.close()
