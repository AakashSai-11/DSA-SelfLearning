def palindrome(i, s):
    if i>=len(s)//2:
        return True
    if s[i] != s[len(s)-i-1]:
        return False
    return palindrome(i+1,s)

print(palindrome(0,'helleh'))
        
        
'''
Palindrome with a twist :-
Here simply put we have to tell if the string can become a palindrome with atmost one swap of characters within the string itself
for -> daeed -> Swapping a with e will result in -> deaed -> This is now a palindrome, So the result should be True as only one swap is done
Two approaches, both can be used, one is mine and one is the solution on the nxtwave platform

'''

#Mine


def canBecomePalindrome(self, s):
    m = set()
    def rev(i,count,s,check):
        if i>=len(s)//2 and count>2:
            return False
        if i>=len(s)//2 and count<=2:
            return check
        if s[i] != s[len(s)-i-1]:
            count += 1
            if len(m)!=0:
                if s[i] in m and s[len(s)-i-1] in m:
                    check = True
                else:
                    check = False
            else:
                m.add(s[i])
                m.add(s[len(s)-i-1])
                if len(s)%2==1 and (s[i] == s[len(s)//2] or s[len(s)-i-1] == s[len(s)//2]):
                    check = True
                else:
                    check = False
        return rev(i+1,count, s, check)
    return rev(0,0,s,True)





#Nxtwave

def canBecomePalindromeRecursive(s, left, right, mismatches):
    # Base case: when pointers cross, check mismatches
    if left >= right:
        if len(mismatches) == 0:
            # No mismatches, string is already a palindrome
            return True
        elif len(mismatches) == 1:
            # One mismatch: check if one mismatched character can match the center character
            first = mismatches[0]
            return (s[first[0]] == s[len(s) // 2] or s[first[1]] == s[len(s) // 2])
        elif len(mismatches) == 2:
            # Two mismatches: check if swapping characters resolves the mismatch
            first = mismatches[0]
            second = mismatches[1]
            return (s[first[0]] == s[second[1]] and s[first[1]] == s[second[0]]) or \
                   (s[first[0]] == s[second[0]] and s[first[1]] == s[second[1]])
    
    if s[left] == s[right]:
        # Characters match, continue checking inner substring
        return canBecomePalindromeRecursive(s, left + 1, right - 1, mismatches)
    else:
        # Characters mismatch, add their indices to mismatches list
        mismatches.append((left, right))
        # If there are more than 2 mismatches, it cannot become a palindrome
        if len(mismatches) > 2:
            return False
        # Continue checking inner substring    
        return canBecomePalindromeRecursive(s, left + 1, right - 1, mismatches)

def canBecomePalindrome(s):
    mismatches = []  # Stores mismatched character indices
    return canBecomePalindromeRecursive(s, 0, len(s) - 1, mismatches)

'''
if __name__ == "__main__":
    s = input()
    print("true" if canBecomePalindrome(s) else "false")
'''