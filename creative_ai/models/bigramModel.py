from creative_ai.utils.print_helpers import ppGramJson


class BigramModel():

    def __init__(self):
        """
        Requires: nothing
        Modifies: self (this instance of the NGramModel object)
        Effects:  This is the NGramModel constructor. It sets up an empty
                  dictionary as a member variable.
        
        This function is done for you.
        """
        self.nGramCounts = {}

    def __str__(self):
        """
        Requires: nothing
        Modifies: nothing
        Effects:  Returns the string to print when you call print on an
                  NGramModel object. This string will be formatted in JSON
                  and display the currently trained dataset.
        
        This function is done for you.
        """

        return ppGramJson(self.nGramCounts)


###############################################################################
# Begin Core >> FOR CORE IMPLEMENTION, DO NOT EDIT ABOVE OF THIS SECTION <<
###############################################################################

    def trainModel(self, text):
        """
        Requires: text is a list of lists of strings
        Modifies: self.nGramCounts, a two-dimensional dictionary. For examples
                  and pictures of the BigramModel's version of
                  self.nGramCounts, see the spec.
        Effects:  this function populates the self.nGramCounts dictionary,
                  which has strings as keys and dictionaries of
                  {string: integer} pairs as values.
                  Returns self.nGramCounts
        """
        # Build a temp dict
        # key: twi continuously word, firstword_secondword
        # value: how many times the words has been seen
        tmp_dict = {}
        for line in text:
            # check the text in every line
            word_list = line
            word_list_len = len(word_list)
            if word_list_len <= 1:
                continue
            # get all two continuously words, from the beginning of line
            for i in range(0, word_list_len - 1):
                # get the two words, and join them as a new key
                first_word = word_list[i]
                second_word = word_list[i + 1]
                tmp_key = "%s_%s" % (first_word, second_word)
                if tmp_key in tmp_dict:
                # the continuously two words has been seen in
                #temp dictionary
                    v = tmp_dict.get(tmp_key, 0)
                    v += 1
                    tmp_dict.update({tmp_key: v})
                else:
                    # the continuously two words first has been seen in text
                    tmp_dict.update({tmp_key: 1})
        # update nGramCounts Value, from the temp dict
        # dict {firstword: {sencondword: value}, }
        for k1, v1 in tmp_dict.items():
            # get the two word from the key in temp dictionary
            k_l = k1.split('_')
            first_word = k_l[0]
            second_word = k_l[1]
            if first_word in self.nGramCounts:
                # if firstword has been a key in nGramCounts
                # dictionary, get the value
                in_dict = self.nGramCounts.get(first_word, {})
                if second_word in in_dict:
                # if second word has been a key in firstword's value,
                    # add 1, and update
                    v = in_dict.get(second_word, 0)
                    v += 1
                    in_dict.update({second_word: v})
                else:
                # second word has not been a key in firstword's value, init it
                    in_dict.update({second_word: 1})
                self.nGramCounts.update({first_word: in_dict})
            else:
            # if firstword not in nGramCounts, init it
                ini_dict = {}
                ini_dict.update({second_word: 1})
                self.nGramCounts.update({first_word: ini_dict})
        return self.nGramCounts


    def trainingDataHasNGram(self, sentence):
        """
        Requires: sentence is a list of strings
        Modifies: nothing
        Effects:  returns True if this n-gram model can be used to choose
                  the next token for the sentence. For explanations of how this
                  is determined for the BigramModel, see the spec.
        """
        #
        lens = len(sentence)
        last_word = sentence[lens - 1]
        # check last word of sentence whether in nGramCounts dictionary
        if keyInDict(self.nGramCounts, last_word):
            return True
        return False

    def getCandidateDictionary(self, sentence):
        """
        Requires: sentence is a list of strings, and trainingDataHasNGram
                  has returned True for this particular language model
        Modifies: nothing
        Effects:  returns the dictionary of candidate next words to be added
                  to the current sentence. For details on which words the
                  BigramModel sees as candidates, see the spec.
        """
        # return the value of key in nGramCounts and the key is the last word
        # in sentence
        lens = len(sentence)
        last_word = sentence[lens - 1]
        if last_word in self.nGramCounts:
            # last word of sentence is a key of nGramCounts dictionary
            return self.nGramCounts.get(last_word, {})
        return {}

###############################################################################
# End Core
###############################################################################

###############################################################################
# Main
###############################################################################

if __name__ == '__main__':
    # remove 'pass' before adding test cases
    # Add your test cases here
    # An example trainModel test case
    bigr = BigramModel()
    text = [['brown', 'blue', 'sky']]
    bigr.trainModel(text)
    # Should print: { 'brown' : {'blue': 1}}
    print(bigr)

    text = [['the', 'brown', 'blue'], ['the', 'lazy', 'dog']]
    bigr.trainModel(text)
    # Should print: { 'the': {'brown': 1, 'lazy': 1}, 'brown': {'blue': 2}, 'lazy': {'dog': 1} , 'blue': {'sky': 1}}
    print(bigr)

    # An example trainingDataHasNGram test case
    bigr = BigramModel()
    sentence = "what a cute lazy"
    print(bigr.trainingDataHasNGram(sentence))  # should be False
    bigr.trainModel(text)
    print(bigr.trainingDataHasNGram(sentence))  # should be True
    print(bigr.getCandidateDictionary(sentence))  #should be {'dog': 1}
    # Add your test cases here
