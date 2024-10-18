def groupAnagrams_abdi(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map = {}
        for s in strs:
            freq = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                freq[idx] += 1

            str_freq = str(freq)
            print(str_freq)
            if str_freq in map.keys():
                map[str_freq] += [s]
            else: map[str_freq] = [s]
        return map.values()
