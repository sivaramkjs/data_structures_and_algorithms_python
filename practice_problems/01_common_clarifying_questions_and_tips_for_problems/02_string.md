1. Can we always expect a valid string? If not (i.e., Null/Empty string) then what should be the output?
2. Is it case-sensitive? Would it contain only lower case or only upper case or both?
3. Can it contain numbers/special characters/Unicode characters?
4. Can there be duplicate characters? or can a character occur multiple times? - (use cases?)

### Tips:

1. In case of string arrays/hash maps, the space complexity will _not_ be just the number of strings in the array/map.
   Since string is not just an atomic unit like numbers, it would be:
    1. "(number of elements) * (length of each string)" ≈ O(number of elements * length of largest string)
    2. It is also good to consider the space for hash map keys as well, especially in case of string keys.
2. Using hash map with **letter frequency key** (e.g., tuple of 26 letters) will be useful for problems based on
   frequency of letters in a string. E.g., Group anagrams, find if a string exists in another random string
3. In case of hash map with just english letter character keys, the space complexity would be O(1) since there would be
   a maximum of 26 keys. Alternatively,we can also use array with fixed-size of 26.
4. In case string encoding/decoding, the time complexity will be the "sum of lengths of all strings" (≈ all characters)
   since we will need to process all characters during encoding and decoding.