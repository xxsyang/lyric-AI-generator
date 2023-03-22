from creative_ai.utils.print_helpers import ppGramJson


class TrigramModel():

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
        Modifies: self.nGramCounts, a three-dimensional dictionary. For
                  examples and pictures of the TrigramModel's version of
                  self.nGramCounts, see the spec.
        Effects:  this function populates the self.nGramCounts dictionary,
                  which has strings as keys and dictionaries as values,
                  where those inner dictionaries have strings as keys
                  and dictionaries of {string: integer} pairs as values.
                  Returns self.nGramCounts
        """
        # Build a temp dict
        # key: three continuously word, firstword_secondword_thirdword
        # value: how many times the words has been seen
        tmp_dict = {}
        for line in text:
            # check the text in every line
            word_list = line
            word_list_len = len(word_list)
            if word_list_len <= 2:
                continue
            # get all three continuously words, from the beginning of line
            for i in range(0, word_list_len - 2):
                # get the three words
                first_word = word_list[i]
                second_word = word_list[i + 1]
                third_word = word_list[i + 2]
                # join the three words as a key
                tmp_key = "%s_%s_%s" % (first_word, second_word, third_word)
                # update the value of key, in the temp dictionary
                if tmp_key in tmp_dict:
                    # if the key has been seen, add 1 on the value, and update
                    v = tmp_dict.get(tmp_key, 0)
                    v += 1
                    tmp_dict.update({tmp_key: v})
                else:
                    # if the key first time has been seen, set the value as 1, and update
                    tmp_dict.update({tmp_key: 1})
        # update nGramCounts Value, from the temp dict
        # dict {firstword: {sencondword: {thirdword: value}}, }
        for k1, v1 in tmp_dict.items():
            # get the firstword, secondword, thirdword from the key in temp dictionary
            words = k1.split('_')
            word_1 = words[0]
            word_2 = words[1]
            word_3 = words[2]
            if word_1 in self.nGramCounts:
                # if firstword has been as a key in  nGramCounts, get value of firstword
                dict_1 = self.nGramCounts.get(word_1, {})
                if word_2 in dict_1:
                    # if secondword has been as a key in the dictionary value of firstword, get value of second word
                    dict_2 = dict_1.get(word_2, {})
                    if word_3 in dict_2:
                        # if thirdword has been as a key in the dictionary, add 1 one the value, and update
                        v = dict_2.get(word_3, 0)
                        v += 1
                        dict_2.update({word_3: v})
                    else:
                        # if thirdword has first been seen as a key, set value as 1, and update
                        dict_2.update({word_3: 1})
                    # update firstword's value with updated secondword's value
                    dict_1.update({word_2: dict_2})
                else:
                    init0_dict = {}
                    init0_dict.update({word_3: 1})
                    dict_1.update({word_2: init0_dict})
                # update value in nGramCounts
                self.nGramCounts.update({word_1: dict_1})
            else:
                # the three word has first been seen , init it
                init_dict = {}
                init_dict2 = {}
                init_dict.update({word_3: 1})
                init_dict2.update({word_2: init_dict})
                self.nGramCounts.update({word_1: init_dict2})
        return self.nGramCounts


    def trainingDataHasNGram(self, sentence):
        """
        Requires: sentence is a list of strings
        Modifies: nothing
        Effects:  returns True if this n-gram model can be used to choose
                  the next token for the sentence. For explanations of how this
                  is determined for the TrigramModel, see the spec.
        """
        # Check the last two word , has been continuously seen in nGramCounts dictionary
        lens = len(sentence)
        if lens < 2:
            return False
        # get the last two words
        last_word = sentence[lens - 1]
        last_two_word = sentence[lens - 2]
        # Check second last word in nGramCounts dictionary
        if last_two_word in self.nGramCounts:
            # Get value of second last word, and check last word whether in it
            dict1 = self.nGramCounts.get(last_two_word, {})
            if last_word in dict1:
                return True
        return False


    def getCandidateDictionary(self, sentence):
        """
        Requires: sentence is a list of strings, and trainingDataHasNGram
                  has returned True for this particular language model
        Modifies: nothing
        Effects:  returns the dictionary of candidate next words to be added
                  to the current sentence. For details on which words the
                  TrigramModel sees as candidates, see the spec.
        """
        # return the value of last two words who has been continuously seen in nGramCounts dictionary
        lens = len(sentence)
        if lens < 2:
            return {}
        # get the last two words
        last_word = sentence[lens - 1]
        last_two_word = sentence[lens - 2]
        # Check second last word in nGramCounts dictionary
        if last_two_word in self.nGramCounts:
            # Get second last word in nGramCounts dictionary
            dict1 = self.nGramCounts.get(last_two_word, {})
            if last_word in dict1:
                # return the value of last word in second last word's value
                return dict1.get(last_word, {})
        # if no value found , return {}
        return {}



###############################################################################
# End Core
###############################################################################

###############################################################################
# Main
###############################################################################

if __name__ == '__main__':
    # An example trainModel test case
    uni = TrigramModel()

    text = [ ['the', 'brown', 'fox'], ['the', 'lazy', 'dog'] ]
    uni.trainModel(text)
    
    print(uni)
    # should print: {'the':{'brown': {'fox': 1}, 'lazy': {'dog': 1}}}

    text = [['the', 'beautiful', 'girl'], ['the', 'lazy', 'dog'], ['give', 'me', 'hug']]
    tri.trainModel(text)
    print(tri)
    # should print: {'the':{'brown': {'fox': 1}, 'lazy': {'dog': 2}, 'beautiful': {'girl': 1}},
    # 'give': {'me': {'hug': 1}}}


    # An example trainingDataHasNGram test case
    tri = TrigramModel()
    sentence = "I like the beautiful"
    print(tri.trainingDataHasNGram(sentence))  # should be False
    tri.trainModel(text)
    print(tri.trainingDataHasNGram(sentence))  # should be True
    print(tri.getCandidateDictionary(sentence))  # should be {'girl': 1}

