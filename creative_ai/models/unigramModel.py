from creative_ai.utils.print_helpers import ppGramJson



def setKeyVal(D, K, V):
    D.update({K: V})
    return D
    
class UnigramModel():

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
        Modifies: self.nGramCounts
        Effects:  this function populates the self.nGramCounts dictionary,
                  which is a dictionary of {string: integer} pairs.
                  For further explanation of UnigramModel's version of
                  self.nGramCounts, see the spec.
                  Returns self.nGramCounts
        """
        # Calcute all word's show time in the whole text, except starting token
        special_token_list = ['^::^', '^:::^']
        for line in text:
            word_list = line
            for word in word_list:
                if word in special_token_list:
                    continue
                if word in self.nGramCounts:
                    v = self.nGramCounts.get(word, 0)
                    v += 1
                    self.nGramCounts.update({word: v})
                else:
                    self.nGramCounts.update({word: 1})
        return self.nGramCounts

    def trainingDataHasNGram(self, sentence):
        """
        Requires: sentence is a list of strings
        Modifies: nothing
        Effects:  returns True if this n-gram model can be used to choose
                  the next token for the sentence. For explanations of how this
                  is determined for the UnigramModel, see the spec.
        """
        # if nGramCounts not empty , return True
        if self.nGramCounts is {}:
            return False
        return True

    def getCandidateDictionary(self, sentence):
        """
        Requires: sentence is a list of strings, and trainingDataHasNGram
                  has returned True for this particular language model
        Modifies: nothing
        Effects:  returns the dictionary of candidate next words to be added
                  to the current sentence. For details on which words the
                  UnigramModel sees as candidates, see the spec.
        """
        # just return nGramCounts as the candidate dictionary
        return self.nGramCounts

###############################################################################
# End Core
###############################################################################

###############################################################################
# Main
###############################################################################

# This is the code python runs when unigramModel.py is run as main
if __name__ == '__main__':

    # An example trainModel test case
    uni = UnigramModel()
    text = [ [ 'brown' ] ]
    uni.trainModel(text)
    # Should print: { 'brown' : 1 }
    print(uni)

    text = [ ['the', 'brown', 'fox'], ['the', 'lazy', 'dog'] ]
    uni.trainModel(text)
    # Should print: { 'brown': 2, 'dog': 1, 'fox': 1, 'lazy': 1, 'the': 2 }
    print(uni)

    # An example trainingDataHasNGram test case
    uni = UnigramModel()
    sentence = "Eagles fly in the sky"
    print(uni.trainingDataHasNGram(sentence)) # should be False
    uni.trainModel(text)
    print(uni.trainingDataHasNGram(sentence)) # should be True
