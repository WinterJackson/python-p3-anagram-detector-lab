# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, anagram_list):
        matched_anagrams = []
        
        for candidate in anagram_list:
            candidate_lower = candidate.lower()
            
            if candidate_lower != self.word and sorted(candidate_lower) == sorted(self.word):
                matched_anagrams.append(candidate)
        
        return matched_anagrams
