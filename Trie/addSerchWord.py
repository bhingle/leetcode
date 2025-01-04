class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.endOfWord = False
        
    def checkDots(self, curr):
        for i in curr.children:
            if i == '.':
                return checkDots

    def search(self, word: str) -> bool:
        curr = self.root
        for letter in word:
            if letter == '.':
                self.checkDots(curr)
            elif letter not in curr.children:
                return False
        return curr.endOfWord


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)