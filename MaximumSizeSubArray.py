#   NAIVE FIRST ATTEMPT
# def lengthOfLongestSubstring(s: str) -> int:

#     max = 0
#     encountered_letters = set()

#     for i in range(len(s)):

#         encountered_letters.add(s[i])
#         substring_candidate = s[i]

#         for j in range(i+1, len(s)):

#             if s[j] not in encountered_letters:
#                 encountered_letters.add(s[j])
#                 substring_candidate += s[j]
#                 print(substring_candidate)

#             else:
#                 encountered_letters.clear()
#                 break

#         candidate_size = len(substring_candidate)
#         if candidate_size > max:
#             max = candidate_size
    
#     return max
    

# testcase = "arwvivbgvtybtnudd"
# print(lengthOfLongestSubstring(testcase))


def lengthOfLongestSubstring(s: str) -> int:

    window_size = 1
    i = 0
    current_window = ""
    letters_map = {}


    while i < len(s):
        
        if s[i] not in letters_map:
            letters_map[s[i]] = i
            current_window += s[i]
            i += 1
            window_size += 1

        else:
            
            # Remove all letters from the front of the current_window until the repeated letter
            while current_window[0] != s[i]:
                del letters_map[current_window[0]]
                current_window = current_window[1:]
            
            # Remove the repeated letter from the current_window
            current_window = current_window[1:]
            
            # Update the index of the repeated letter in the letters_map
            letters_map[s[i]] = i
            
            # Update the window size
            window_size = len(current_window)
            
            i += 1
    
    return window_size



        # letters_map = {}
        # max_length = 0
        # start = 0

        # for i in range(len(s)):
        #     if s[i] in letters_map and letters_map[s[i]] >= start:
        #         start = letters_map[s[i]] + 1
        #     letters_map[s[i]] = i
        #     max_length = max(max_length, i - start + 1)

        # return max_length
