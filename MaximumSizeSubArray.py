def lengthOfLongestSubstring(s: str) -> int:

    max = 0
    encountered_letters = set()

    for i in range(len(s)):

        encountered_letters.add(s[i])
        substring_candidate = str(i)

        for j in range(i+1, len(s)):

            if s[j] not in encountered_letters:
                encountered_letters.add(s[j])
                substring_candidate += s[j]

            else:
                break

        candidate_size = len(substring_candidate)
        if candidate_size > max:
            max = candidate_size
    
    return max
    