import re

text = "cat mat bat rat"
pattern = 'cart'

# re.findall(pattern, text)
output = re.findall(pattern, text)
print(output)

text_1 = "cat mat bat rat cat"
output_1 = re.findall(pattern, text_1)
print(output_1)

text = 'abc 123 8y9y988uu'
pattern = r'[\d]'  # for extracting numbers
print(re.findall(pattern, text))

text = 'abc def ghi jkl'
pattern = r'[def]'  # for extracting the string put outputting it individually
print(re.findall(pattern, text))

text = 'Hello World! abc DEF 123'
pattern = r'[A-Z]'  # for extracting upper case letters [a-z] for lowercase
print(re.findall(pattern, text))

text = 'abc def ghi jkl'
pattern = r'[^def]'  # ^ apart from
print(re.findall(pattern, text))

text = 'abc  \t def ghi \t jkl'
pattern = r'[^def]'  #
print(re.findall(pattern, text))
text = 'Hello World 1234 ^&**%$'
# pattern = r'[^A-z0-9]' extract the symbols
pattern = r'[^A-z0-9\s]'  # \s to extract the spaces
print(re.findall(pattern, text))

# SPECIAL CHARACTERS
text = 'dello World hallo heeello'
pattern = r'h.*llo'  # start with h . (one space) ends with llo
print(re.findall(pattern, text))

text = 'dello World hallo heeello'
pattern = '.*ld'
print(re.findall(pattern, text))

# QUANTIFIERS
text = 'a aa aaa aaaa aaaaa'
# pattern = 'a*'  # extract for matches of 0 and more
pattern = r'a{3,}'  # extract for matches of 1 and more r'a{3,}' 3 or more
print(re.findall(pattern, text))

pattern = r'a{2,4}'  # extract for matches of 2 and 4 and more r'a{3,}' 3 or more
print(re.findall(pattern, text))

# substituting
text = 'Daniel and marvelous are best friends'
pattern = 'friends'
print(re.sub(pattern, 'opps', text))

# COMPILING REGULAR EXPRESSIONS

text = 'There are 10 apples and 20 oranges'
pattern = '[0-9]'
print(re.findall(pattern, text))

text = 'There are 10 apples and 20 oranges'
pattern = r'\d+'
print(re.findall(pattern, text))

pattern = r'\d+'
text = 'There are 90 apples and 20 oranges'
output = re.compile(pattern).findall(text)
print(output)

text = 'There are 10 apples and 20 oranges'
pattern = '[A-z]+'
print(re.findall(pattern, text))

text = 'There are 10 apples and 20 oranges'
pattern = r'[\w]+'
print(re.findall(pattern, text))


# SPLIT FUNCTION

text = 'split this text for me right away'
pattern = r'\s+'
print(re.split(pattern, text))
print(text.split('t'))
