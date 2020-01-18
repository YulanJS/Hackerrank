"""
# beautiful string
import math
import os
import random
import re
import sys
# idea: don't split string into numbers, make up a new string
# with increasing numbers, and compare it with old string


def separateNumbers(s):
    if len(s) == 1:
        print("NO")
        return
    for i in range(1, len(s)//2 + 1):
        myList = [s[:i]]
        while len(''.join(myList)) < len(s):
            myList.append(str(int(myList[-1]) + 1))
        print(''.join(myList))

        if ''.join(myList) == s:
            print("YES" + " " + myList[0])
            return
    print("NO")


if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s = input()
        separateNumbers(s)
"""

"""
# palindrome index
#!/bin/python3

import math
import os
import random
import re
import sys


def isPalindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True


def palindromeIndex(s):
    if isPalindrome(s):
        return -1
    str = s
    start = 0
    end = len(s) - 1
    while len(str) > 1:
        if str[0] == str[-1]:
            str = str[1: -1]
            start += 1
            end -= 1
        elif isPalindrome(str[1:]):
            return start
        elif isPalindrome(str[:-1]):
            return end
        else:
            return -1
    return -1


if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = palindromeIndex(s)
        print(result)
"""


"""
import math
import os
import random
import re
import sys
# I tried, get letter_frequency_dict and get frequency_letter_dict,
# actually, we don't care one frequency correspond to which letters.
# we just care how many letters have this frequency.
# use Counter and list.count
from collections import Counter


def isValid(s):
    letter_frequency = Counter(s)
    freq_list = letter_frequency.values()
    # think of this as dict of frequency: letter, but we don't care what specific letters are there
    # we only care how many distinct letter symbols are there
    freq_num_letters = Counter(freq_list)
    if len(freq_num_letters) == 1:
        return "YES"
    if len(freq_num_letters) > 2:
        return "NO"
    # aaabbbdddc min frequency is one, and there is only one letter corresponds to this frequency,
    # just delete it
    if min(freq_num_letters) == 1 and freq_num_letters[min(freq_num_letters)] == 1:
        return "YES"
    # aaabbccdd max frequency letter is one more than other frequencies,
    # and there is only one letter has max frequency
    if freq_num_letters[max(freq_num_letters)] == 1 and max(freq_num_letters) - min(freq_num_letters) == 1:
        return "YES"
    return "NO"


if __name__ == '__main__':
    s = input()
    result = isValid(s)
    print(result)
"""

'''
# longest common sequence, dynamic programming, find recursive relations first
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    c = [[0] * (len(s2) + 1) for _ in range(2)]
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                c[i % 2][j] = c[(i - 1) % 2][j - 1] + 1
            else:
                c[i % 2][j] = max(c[(i - 1) % 2][j], c[i % 2][j - 1])
    return c[len(s1) % 2][len(s2)]


if __name__ == '__main__':
    s1 = input()
    s2 = input()
    result = commonChild(s1, s2)
    print(result)
'''

"""
# highest value palindrome
# recursive version, may not be right, times out
import math
import os
import random
import re
import sys

# Complete the highestValuePalindrome function below.
def highestValuePalindrome(s, k):
    if k < 0:
        return -1
    if k == 0 and s[::-1] != s:
        return -1
    if k == 0:
        return int(s)
    if len(s) == 1:
        return 9
    if s[0] == s[-1]:
        if len(s) == 2:
            if k >= 2:
                return 99
            return int(s)
        middle1 = highestValuePalindrome(s[1:-1], k)
        middle2 = highestValuePalindrome(s[1:-1], k - 2)
        if middle1 == -1 and middle2 == -1:
            return -1
        if middle2 == -1:
            return int(s[0] + str(middle1) + s[-1])
        if middle1 == -1:
            return int('9' + str(middle2) + '9')
        return max(int(s[0] + str(middle1) + s[-1]), int('9' + str(middle2) + '9'))
    if s[0] != s[-1]:
        if len(s) == 2:
            if k >= 2:
                return 99
            else:
                return int(max(s[0], s[-1]) + max(s[0], s[-1]))
        middle1 = highestValuePalindrome(s[1: -1], k - 1)
        middle2 = highestValuePalindrome(s[1: -1], k - 2)
        if middle1 == -1 and middle2 == -1:
            return -1
        if middle1 == -1:
            return int('9' + str(middle2) + '9')
        if middle2 == -1:
            return int(max(s[0], s[-1]) + str(middle1) + max(s[0], s[-1]))
        return max(int(max(s[0], s[-1]) + str(middle1) + max(s[0], s[-1])), int('9' + str(middle2) + '9'))


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    s = input()
    result = highestValuePalindrome(s, k)
    print(result)
"""

"""
# highest value palindrome
# !/bin/python3
import math
import os
import random
import re
import sys
# Complete the highestValuePalindrome function below.
# first convert to a palindrome, then check how many changes are remained.
# I did it myself! With some help from testcases. It used up a long time.
# However, it exactly match the idea provided in discussion board. Good job!
# After change change_list to num_changes, time out problem never occurred.
def highestValuePalindrome(s, k):
    result = ""
    num_changes = 0
    # change result with first round loop, then second time, it can stop
    # while remained_changes is 0. Second loop only revise some digits to 9.
    # no need to create a change_list [] to reflect whether each digit is
    # changed or not, because by comparing s[i] and s[len(s) - 1 - i],
    # we can know whether a digit must have to change to make it a palindrome or not.
    # First step: change it to palindrome. Using minimum num of changes.
    for i in range(len(s)//2):
        if num_changes > k:
            return '-1'
        if s[i] != s[len(s) - 1 - i]:
            num_changes += 1
            result += max(s[i], s[len(s) - 1 - i])
        else:
            result += s[i]
    remained_changes = k - num_changes
    # If no remained_changes, no need for second step.
    if remained_changes < 0:
        return '-1'
    # Second step: change palindrome to max palindrome. Changing some digits to 9.
    curr_index = 0
    while remained_changes > 0 and curr_index < len(s) // 2:
        # is_changed: to see whether the digit s[curr_index]
        # has to change to make palindrome in first step
        is_changed = 0
        if s[curr_index] != s[len(s) - 1 - curr_index]:
            # it is changed in the first step, used one chance of change.
            is_changed = 1
        # if you changed in the first step, return the chances back to you to see if it is
        # enough to change two digits to 9 ... 9.
        temp = remained_changes + is_changed - 2
        # Be careful here, we only need to change to 9 ... 9
        # when it is not changed to 9 in the first step.
        if temp >= 0 and result[curr_index] != '9':
            result = result[:curr_index] + '9' + result[curr_index + 1:]
            remained_changes = temp
        curr_index += 1
    if len(s) % 2:
        # for string with odd length, may need to change the middle digit if chance_remained
        if remained_changes > 0:
            result += '9' + result[::-1]
        else:
            result += s[len(s) // 2] + result[::-1]
    else:
        # string with even length
        result += result[::-1]
    return result


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    s = input()
    result = highestValuePalindrome(s, k)
    print(result)
"""


"""
# bear and steady gene
from collections import Counter


def min_window(s, t):
    # minWindow algorithm
    # s: string t: required pattern
    need = Counter(t)
    left_pointer, right_pointer, left_result, right_result, missing = 0, 0, 0, 0, len(t)
    while right_pointer < len(s):
        # move rightPointer
        # rightPointer points to the position right after the right bound of the window we found
        # rightPointer also means it is the next position to check if we need to move rightPointer or not
        # beautiful design of need and missing: need dict value can be negative to record repeated item
        # use missing to show if all found or not
        if s[right_pointer] in need:
            if need[right_pointer] > 0:
                missing -= 1
            # need may be negative to record repeated items
            need[s[right_pointer]] -= 1
        right_pointer += 1
        while missing == 0:
            # move leftPointer
            if right_result == 0 or right_pointer - left_pointer < right_result - left_result:
                # leftResult, rightResult stores the previously found minWindow
                # if rightResult == 0, it is the first minWindow found
                left_result, right_result = left_pointer, right_pointer
            if s[left_pointer] in need:
                need[s[left_pointer]] += 1
                if need[s[left_pointer]] > 0:
                    missing += 1
            left_pointer += 1
    return s[left_result: right_result]
"""


"""
# bear and steady gene
import math
import os
import random
import re
import sys
from collections import Counter


def steadyGene(gene):
    frequency = Counter(gene)
    need = {}
    num_to_replace = 0
    for letter in frequency:
        if frequency[letter] > len(gene) // 4:
            need[letter] = frequency[letter] - len(gene) // 4
            num_to_replace += need[letter]
    if not need:
        return 0
    left_pointer, right_pointer, left_result, right_result = 0, 0, 0, 0
    while right_pointer < len(gene):
        if gene[right_pointer] in need:
            if need[gene[right_pointer]] > 0:
                num_to_replace -= 1
            need[gene[right_pointer]] -= 1
        right_pointer += 1
        while num_to_replace == 0:
            if right_result == 0 or right_pointer - left_pointer < right_result - left_result:
                left_result, right_result = left_pointer, right_pointer
            if gene[left_pointer] in need:
                need[gene[left_pointer]] += 1
                if need[gene[left_pointer]] > 0:
                    num_to_replace += 1
            left_pointer += 1
    return right_result - left_result


if __name__ == '__main__':
    n = int(input())
    gene = input()
    result = steadyGene(gene)
    print(result)
"""


"""
# sherlock and anagrams
#!/bin/python3
import math
import os
import random
import re
import sys
from collections import Counter
# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    # brute force, list all possible substrings, sort them before putting into dictionary
    count = 0
    for i in range(1, len(s) + 1):
        #  i same, same length substring
        same_length_substrings = [''.join(sorted(s[j: j + i])) for j in range(len(s) - i + 1)]
        same_length_freq = Counter(same_length_substrings)
        for str in same_length_freq:
            count += same_length_freq[str] * (same_length_freq[str] - 1) // 2
    return count


if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = sherlockAndAnagrams(s)
        print(result)
"""

"""
# maximum palindromes
# It is not done yet, some testcases get timed out in Hackerrank, however, my laptop can run
# and can get correct results
#!/bin/python3
import math
import os
import random
import re
import sys
from collections import Counter


class MaximumPalindrome:

    def __init__(self, s):
        # required by problem, some numbers too big, just mod a big prime
        self.NUM_TO_MOD = pow(10, 9) + 7
        self.s = s
        # 2d frequency list, cols: letter a - z
        # rows: we just pre-calculate frequency once for any number of queries about the same string s
        # rows: queries about different substrings.
        # substring[l - 1: r], then just use row[r - 1] - row[l - 2]
        # pre-calculate frequency is a frequently used trick
        # a dict: use i to represent substring s[0: i + 1]: dict(letters of substring: frequency)
        self.frequency = {i: {} for i in range(len(s))}
        for i in range(len(s)):
            if i > 0:
                # each row duplicates the previous row and add frequency for current letter
                self.frequency[i] = self.frequency[i - 1].copy()
            self.frequency[i][s[i]] = self.frequency[i].get(s[i], 0) + 1
        # pre-compute factorial, frequently used trick. Calculating factorials frequently makes code slow.
        # Therefore, pre-compute factorials.
        self.factorials = self.compute_factorial(self.frequency[-1])

    def exp_mod(self, a, p, n):
        # chapter 31(CLRS), calculate a ^ p mod n
        c = 0
        d = 1
        binary_form_reverse = []
        while p > 0:
            binary_form_reverse.append(p % 2)
            p = p // 2
        for i in range(len(binary_form_reverse)):
            c = 2 * c
            d = d * d % n
            if binary_form_reverse[len(binary_form_reverse) - 1 - i] == 1:
                c = c + 1
                d = d * a % n
        return d

    def compute_factorial(self, a_list):
        # this number is demanded based on math formula, will explain in details later
        largest = sum(elem // 2 for elem in a_list)
        fact = [1 for _ in range(largest + 1)]
        for i in range(2, largest + 1):
            fact[i] = fact[i - 1] * i % self.NUM_TO_MOD
        return fact

    def answerQuery(self, l, r):
        freq = [0] * 26
        num_of_rows = len(self.s)
        if l >= 2:
            for letter in self.frequency[min(r - 1, num_of_rows - 1)]:
                # it seems that some r is out of list range, to be safe use min here
                freq[letter] = self.frequency[min(r - 1, num_of_rows - 1)][letter] - self.frequency[min(l - 2, num_of_rows - 1)].get(letter, 0)
        else:
            # if l = 1, starting from the first row, no need to minus two rows
            freq = self.frequency[min(r - 1, num_of_rows - 1)].copy()
        # distribution a dict: frequency: number of distinct letters have this frequency
        # compare to dict: frequency: letters
        # which letters have this frequency does not matter, only nums of them matters
        distribution = Counter(freq)    
        odd_freq_letter_count = 0
        # delete letters with 0 frequency
        del distribution[0]
        # for letters with odd frequency, by math, we can use at most one letter at the middle to
        # make maximum length palindrome. It has odd_freq_letter_count possibilities for the middle letter.
        # For letters with odd frequency, frequency // 2 of these letters will be used in permutation
        # in the left half, (right half is the same for palindrome, ignore right)
        for frequencies in distribution:
            if frequencies % 2:
                odd_freq_letter_count += distribution[frequencies]
        count = 0
        # math formula: n! / (p! q! r!) num of permutations with repeated letters
        # odd or even frequency does not matter here, they are both frequency //2
        # count is the total n
        for frequencies in distribution:
            # how many distinct letters have this frequency, multiply
            count += (frequencies // 2) * distribution[frequencies]
        # check from pre-computed factorial list
        count = self.factorials[count]
        for frequencies in distribution:
            if frequencies > 1:
                # just to ignore those letters with odd frequency 1, frequency // 2 = 0
                # no need to calculate exp_mod
                # n! /(p!q!r!) modular arithmetic: 1/p!: modular inverse of p!, 
                # a^(prime - 1) = 1 mod prime. modular inverse of a mod prime is a^(prime - 2)
                a = self.factorials[frequencies // 2]
                a_pow_p_minus_2 = self.exp_mod(a, self.NUM_TO_MOD - 2, self.NUM_TO_MOD)
                # repeat the process for letters with same frequencies n!/p!p!p!q!q!r!r!r!r!
                for _ in range(distribution[frequencies]):
                    count = count * a_pow_p_minus_2 % self.NUM_TO_MOD
        # multiply possibilities for the middle letter
        if odd_freq_letter_count > 0:
            count = count * odd_freq_letter_count % self.NUM_TO_MOD
        return int(count)


if __name__ == '__main__':1
    s = input()
    mp = MaximumPalindrome(s)
    q = int(input().strip())
    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        l = int(first_multiple_input[0])
        r = int(first_multiple_input[1])
        result = mp.answerQuery(l, r)
        print(result)
# tricks for this problem: math formula, modular inverse, pre-compute factorial, 
# pre-compute frequency for different substrings. May be possible to do better, still times out.
"""

