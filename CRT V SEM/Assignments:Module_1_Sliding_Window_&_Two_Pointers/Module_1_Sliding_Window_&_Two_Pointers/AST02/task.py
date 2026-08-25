def isPalindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return is_palindrome_range(s, left + 1, right) or \
                   is_palindrome_range(s, left, right - 1)

        left += 1
        right -= 1

    return True


def is_palindrome_range(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


if __name__ == '__main__':
    n = int(input())
    s = input().strip()
    print(isPalindrome(s))