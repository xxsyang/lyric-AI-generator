import json

def copy_ngram_dict(parent_dict, new_dict = {}, trained_values = None):
    """
    Recurses through ngram style dictionary, casting each key/value
    to equivalent string in order to be parsed as json.
    """

    for k, v in parent_dict.items():

        if not isinstance(v, dict):
            new_dict[repr(k)] = v

            if isinstance(trained_values, list):
                trained_values[0] = trained_values[0] + 1

        else:
            new_dict[repr(k)] = {}
            copy_ngram_dict(parent_dict[k], new_dict[repr(k)], trained_values)


def key_value_pairs(parent_dict):

    values = [0]
    copy_ngram_dict(parent_dict, trained_values=values)

    return values[0]


def ppGramJson(ngram):
    """
    Pretty print given ngram as json.
    """

    pdict = {}

    copy_ngram_dict(ngram, pdict)

    ppitem = json.dumps(
        pdict,
        sort_keys=True,
        indent=4,
        separators=(',', ': ')
    )

    return ppitem


def ppListJson(data):

    ppitem = json.dumps(
        data,
        sort_keys=True,
        indent=4,
        separators=(',', ': ')
    )

    return ppitem