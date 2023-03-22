import random
from creative_ai.data.dataLoader import prepData
from creative_ai.models.unigramModel import UnigramModel
from creative_ai.models.bigramModel import BigramModel
from creative_ai.models.trigramModel import TrigramModel
from creative_ai.utils.print_helpers import key_value_pairs


class LanguageModel():

    def __init__(self, models=None):
        """
        Requires: nothing
        Modifies: self (this instance of the LanguageModel object)
        Effects:  This is the LanguageModel constructor. It sets up an empty
                  dictionary as a member variable.
        
        This function is done for you.
        """

        if models != None:
            self.models = models
        else:
            self.models = [TrigramModel(), BigramModel(), UnigramModel()]

    def __str__(self):
        """
        Requires: nothing
        Modifies: nothing
        Effects:  This is a string overloaded. This function is
                  called when languageModel is printed.
                  It will show the number of trained paths
                  for each model it contains. It may be
                  useful for testing.
        
        This function is done for you.
        """

        output_list = [
            '{} contains {} trained paths.'.format(
                model.__class__.__name__, key_value_pairs(model.nGramCounts)
                ) for model in self.models
            ]

        output = '\n'.join(output_list)

        return output

    def updateTrainedData(self, text, prepped=True):
        """
        Requires: text is a 2D list of strings
        Modifies: self (this instance of the LanguageModel object)
        Effects:  adds new trained data to each of the languageModel models.
        If this data is not prepped (prepped==False) then it is prepepd first
        before being passed to the models.

        This function is done for you.
        """

        if (not prepped):
            text = prepData(text)

        for model in self.models:
            model.trainModel(text)


###############################################################################
# Begin Core >> FOR CORE IMPLEMENTION, DO NOT EDIT ABOVE OF THIS SECTION <<
###############################################################################

    def selectNGramModel(self, sentence):
        """
        Requires: self.models is a list of NGramModel objects sorted by descending
                  priority: tri-, then bi-, then unigrams.

                  sentence is a list of strings.
        Modifies: nothing
        Effects:  returns the best possible model that can be used for the
                  current sentence based on the n-grams that the models know.
                  (Remember that you wrote a function that checks if a model can
                  be used to pick a word for a sentence!)
        """
        # Check TrigramModel whether can provide a candidate dictionary
        for m in self.models:
            model_name = m.__class__.__name__
            if model_name == "TrigramModel":
                if m.trainingDataHasNGram(sentence):
                    return m

        # Check BigramModel whether can provide a candidate dictionary
        for m in self.models:
            model_name = m.__class__.__name__
            if model_name == "BigramModel":
                if m.trainingDataHasNGram(sentence):
                    return m

        # Check trainingDataHasNGram whether can provider a candidate dictionary
        for m in self.models:
            model_name = m.__class__.__name__
            if model_name == "UnigramModel":
                if m.trainingDataHasNGram(sentence):
                    return m
        # if no Model can provider a candidate dictionary, return None
        return None


    def weightedChoice(self, candidates):
        """
        Requires: candidates is a dictionary; the keys of candidates are items
                  you want to choose from and the values are integers
        Modifies: nothing
        Effects:  returns a candidate item (a key in the candidates dictionary)
                  based on the algorithm described in the spec.
        """
        keys_list = []    # select all keys in candidate dictionary as list
        val_list = []     # select all values in candidate dictionary as list
        weight_list = []

        # Prepare keys list and values list
        for key, val in candidates.items():
            keys_list.append(key)
            val_list.append(val)

        sum_value = 0  # sum is cumulative value, start with 0
        # compute the cumulative value, and all values as list sorted
        for i in range(0, len(keys_list)):
            sum_value += val_list[i]
            weight = sum_value
            weight_list.append(weight)
        # get a random value between 0 and the maximum cumulative value
        random_value = random.randrange(0, sum_value)
        # Check the cumulative values weight_list, and get the index of the value,
        # who is first value larger than the randmon value
        index = len(weight_list)
        for i in range(0, len(weight_list)):
            if weight_list[i] > random_value:
                index = i
                break
        # return the key value in keys_list, selected by the index calculated out
        # In other word, return the word which will add into the sentence
        return keys_list[index]



    def getNextToken(self, sentence, filter=None):
        """
        Requires: sentence is a list of strings, and this model can be used to
                  choose the next token for the current sentence
        Modifies: nothing
        Effects:  returns the next token to be added to sentence by calling
                  the getCandidateDictionary and weightedChoice functions.
                  For more information on how to put all these functions
                  together, see the spec.

                  If a filter is being used, and none of the models
                  can produce a next token using the filter, then a random
                  token from the filter is returned instead.
        """
        # First, get a effective model from all models
        select_model = self.selectNGramModel(sentence)
        # Second, get a candidate dictionary with the selected model
        candidata_dict = select_model.getCandidateDictionary(sentence)
        # Third, return the next token for sentence
        if candidata_dict is None:
            # if no candidate can be found , end the sentence
            print("error")
            return '$:::$'
        else:
            if filter is None:
                # if no filter , just return the word
                word = self.weightedChoice(candidata_dict)
                return word
            else:
                # situation filter is not None
                filter_candidate = {}
                special_token_list = ['^::^', '^:::^', '$:::$']
                # Prepare the final candidate dictionary with filter
                # Build a new dictionary who key in candidate dictionary also as a member of filter
                # and value is same value in candidate dictionary
                for key, val in candidata_dict.items():
                    if key in special_token_list:
                        setKeyVal(filter_candidate, key, val)
                        continue
                    if key in filter:
                        setKeyVal(filter_candidate, key, val)
                # return the next token
                if filter_candidate is {}:
                    # if final candidate dictionary is empty ,return a random value of filter as the next token
                    random_value = random.randrange(0, len(filter))
                    return filter[random_value]
                else:
                    # get next token with new final candidate dictionary, and return
                    filter_word = self.weightedChoice(filter_candidate)
                    return filter_word

###############################################################################
# End Core
###############################################################################

###############################################################################
# Main
###############################################################################

if __name__ == '__main__':
    # remove 'pass' before adding test cases
    languageMode = LanguageModel(TrigramModel())
    text = [['the', 'brown', 'fox'], ['the', 'lazy', 'dog']]
    languageMode.trainModel(text)
    print(languageMode)
    # should print: {'the':{'brown': {'fox': 1}, 'lazy': {'dog': 1}}}

    text = [['the', 'beautiful', 'girl'], ['the', 'lazy', 'dog'], ['give', 'me', 'hug']]
    languageMode.trainModel(text)
    print(languageMode)
    # should print: {'the':{'brown': {'fox': 1}, 'lazy': {'dog': 2},
    #'beautiful': {'girl': 1}},
    # 'give': {'me': {'hug': 1}}}


    # An example trainingDataHasNGram test case
    languageMode = LanguageModel(TrigramModel())
    sentence = "I like the beautiful"
    print(languageMode.trainingDataHasNGram(sentence))  # should be False
    languageMode.trainModel(text)
    print(languageMode.trainingDataHasNGram(sentence))  # should be True
    print(languageMode.getNextToken(sentence))          # should be girl

