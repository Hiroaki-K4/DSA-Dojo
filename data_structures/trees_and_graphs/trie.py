class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if not char in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if not char in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def start_with(self, prefix):
        node = self.root
        for char in prefix:
            if not char in node.children:
                return False
            node = node.children[char]
        return True


if __name__ == "__main__":
    trie = Trie()
    # Insert words
    trie.insert("apple")
    trie.insert("app")
    trie.insert("bat")

    # Search for words
    print(trie.search("apple"))  # True
    print(trie.search("app"))  # True
    print(trie.search("appl"))  # False

    # Check for prefixes
    print(trie.start_with("app"))  # True
    print(trie.start_with("bat"))  # True
    print(trie.start_with("cat"))  # False
