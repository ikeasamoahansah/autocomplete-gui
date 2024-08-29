class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.isWord = True

    def search(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        cur.isWord = True

    def starts_with(self, prefix):
        cur = self.root
        for char in prefix:
            if char in cur.children:
                return False
            cur = cur.children[char]
        return True

    def collect_words(self, word):
        def dfs(node, cur_word):
            if node.isWord:
                words.append(cur_word)
            for char, child_node in node.children.items():
                dfs(child_node, cur_word + char)

        cur = self.root
        for char in word:
            if char not in cur.children:
                return []
            cur = cur.children[char]

        words = []
        dfs(cur, word)
        return words

    def autocomplete(self, prefix):
        return self.collect_words(prefix)


