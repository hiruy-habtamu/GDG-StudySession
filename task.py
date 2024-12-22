def WordCount(sentence):
    sentence_list = sentence.split()
    for word in sentence_list:
        print(word + " = " + str(sentence.count(word)))
