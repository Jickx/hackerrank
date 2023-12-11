def trans_form_sentence(sentence):
    alpbt = 'abcdefghijklmnopqrstuvwxyz'
    sen_list = sentence.split()
    result = []
    for word in sen_list:
        new_word = ''
        for i, letter in enumerate(word):
            if i == 0:
                new_word += letter
            elif letter.lower() == word[i - 1].lower():
                new_word += letter
            elif (alpbt.index(letter.lower()) >
                  alpbt.index(word[i - 1].lower())):
                new_word += letter.upper()
            elif (alpbt.index(letter.lower()) <
                  alpbt.index(word[i - 1].lower())):
                new_word += letter.lower()
        result.append(new_word)
    return ' '.join(result)


sentence = 'a Blue MOON'
assert trans_form_sentence(sentence) == 'a BLUe MOOn'
