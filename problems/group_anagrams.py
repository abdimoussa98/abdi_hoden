
def char_frequency(self, str1):
        dict = {}
        for n in str1:
            keys = dict.keys()
            if n in keys:
                dict[n] += 1
            else:
                dict[n] = 1
        return dict
def groupAnagrams(self, strs):
    dict = {}
    for str in strs:
        char_array = list(str)
        frequency_map = frozenset(self.char_frequency(char_array).items())
        if frequency_map in dict:
                dict.setdefault(frequency_map, dict[frequency_map].append(str))
        else:
                dict.setdefault(frequency_map, [str])

    return dict.values()