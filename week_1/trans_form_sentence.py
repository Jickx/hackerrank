def trans_form_sentence(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    sen_list = sentence.split()
    result = []
    for word in sen_list:
        new_word = ''
        for i, letter in enumerate(word):
            if i == 0:
                new_word += letter
            elif letter.lower() == word[i - 1].lower():
                new_word += letter
            elif alphabet.index(letter.lower()) > alphabet.index(word[i - 1].lower()):
                new_word += letter.upper()
            elif alphabet.index(letter.lower()) < alphabet.index(word[i - 1].lower()):
                new_word += letter.lower()
        result.append(new_word)
    return ' '.join(result)


sentence = 'a Blue MOON'
assert trans_form_sentence(sentence) == 'a BLUe MOOn'
