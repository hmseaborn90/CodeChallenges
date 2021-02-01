class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        possible_punctuation = "!?',;."
        
        # remove punctuation from paragraph
        for symbol in possible_punctuation: 
            if symbol in paragraph: 
                paragraph = paragraph.replace(symbol, " ")
        
        # cast paragraph to lowercase 
        lowercase_paragraph = paragraph.lower().split()
        count_words = {}
        
        # get a count of the words in paragraph 
        for word in lowercase_paragraph:
            if word in banned:
                continue 
            if word not in count_words.keys():
                count_words[word] = 1 
            else:
                count_words[word] += 1
        
        max_word = str(max(count_words, key=count_words.get))
        
        return(max_word)


#better solution
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        #1). replace the punctuations with spaces,
        #      and put all letters in lower case
        normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])

        #2). split the string into words
        words = normalized_str.split()

        word_count = defaultdict(int)
        banned_words = set(banned)

        #3). count the appearance of each word, excluding the banned words
        for word in words:
            if word not in banned_words:
                word_count[word] += 1

        #4). return the word with the highest frequency
        return max(word_count.items(), key=operator.itemgetter(1))[0]