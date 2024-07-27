def lengthOfLongestSubstring (s: str) -> int:
    
    characters = {}

    for i in range(len(s)):

        s_value = s[i]
        if s_value in characters:
            i += 1
            continue

        # Currently stores the number of occurances. 
        # could use index of letter within the str??
        characters[s_value] = 1
