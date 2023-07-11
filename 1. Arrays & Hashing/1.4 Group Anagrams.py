class AnagramGrouper:
    def groupAnagrams(self, list_of_words):
        new_dict = {}
        for word in list_of_words:
            sorted_word = ''.join(sorted(word))
            if sorted_word in new_dict:
                new_dict[sorted_word].append(word)
            else:
                new_dict[sorted_word] = [word]
        return list(new_dict.values())


# Test the function with some sample data
anagram_grouper = AnagramGrouper()

# Sample input
list_of_words = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Group the anagrams
result = anagram_grouper.groupAnagrams(list_of_words)

# Print the groups of anagrams
for group in result:
    print(group)
