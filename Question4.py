handle = open("mbox-short.txt", "r")

handle_list = handle.readlines()

dictionary = dict()

for i in range(len(handle_list)):
    word_list = handle_list[i].split()
    for word in word_list:
        if "@" in word:
            sepr = word.split("@")
            dictionary[sepr[1]] = dictionary.get(sepr[1], 0) + 1

print(dictionary)

handle.close()