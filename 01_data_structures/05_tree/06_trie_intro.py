# Trie (Prefix Tree):
#   1. A specialized data structure used in searching, specifically text search.
#   2. It can outperform binary tree, hash table based on the type of searching (e.g., text)
#   3. It allows us to know if a word or part of a word exits in a body of text.
#   4. It has an empty/start node, can have multiple children.
#   E.g., Search engine auto completions, Dictionary search, IP routing
#                     start
#             /     |     |     \
#           A       D     N      Z
#         /  \     /     / \      \
#       R     S  O      E   O      E
#     /         /     /      \      \
#    E         T     W        T      N
#                  /
#                 S

# Time Complexity: O(length of word)
# Space Complexity: Since we use prefixes (e.g., each alphabet node), we don't need to store same letter multiple times in a subtree
#                   (e.g., 'N' in NEWS and NOT).
