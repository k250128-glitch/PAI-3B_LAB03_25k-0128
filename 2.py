def is_anagram(s, t):
    if len(s) != len(t):
        return False

    freq_s = {}
    freq_t = {}

    for ch in s:
        freq_s[ch] = freq_s.get(ch, 0) + 1

    for ch in t:
        freq_t[ch] = freq_t.get(ch, 0) + 1

    return freq_s == freq_t


s = "listen"
t = "silent"
print(is_anagram(s, t))
