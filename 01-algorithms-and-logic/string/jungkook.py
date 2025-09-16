jungkook = "Jungkook"
letters = list(jungkook)
for char in letters[:6]:
    print('\t', char)
for char in letters[-7:]:
    print('\t' * 2, char)
for char in letters[0:len(jungkook)]:
    print('\t' * 3, char)

print('\n' + jungkook)
