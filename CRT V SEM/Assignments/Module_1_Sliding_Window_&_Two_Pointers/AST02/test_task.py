def Check_Palindrome(S):
    left = 0
    right = len(S) - 1

    while left < right:
        if S[left] != S[right]:
            # Try deleting either the left or right character
            return (
                S[left + 1:right + 1] == S[left + 1:right + 1][::-1]
                or
                S[left:right] == S[left:right][::-1]
            )

        left += 1
        right -= 1

    return True