def anagram():
    w1 = input("Enter a word: ").lower()
    w2 = input("Enter a word: ").lower()
    if sorted(w1) == sorted(w2):
        print(f"{w1} and {w2} are anagrams.")
    else:
        print(f"{w1} and {w2} are not anagrams.")


anagram()