import re


DEBURRED_LETTERS = {
  '\xc0': 'A',
  '\xc1': 'A',
  '\xc2': 'A',
  '\xc3': 'A',
  '\xc4': 'A',
  '\xc5': 'A',
  '\xe0': 'a',
  '\xe1': 'a',
  '\xe2': 'a',
  '\xe3': 'a',
  '\xe4': 'a',
  '\xe5': 'a',
  '\xc7': 'C',
  '\xe7': 'c',
  '\xd0': 'D',
  '\xf0': 'd',
  '\xc8': 'E',
  '\xc9': 'E',
  '\xca': 'E',
  '\xcb': 'E',
  '\xe8': 'e',
  '\xe9': 'e',
  '\xea': 'e',
  '\xeb': 'e',
  '\xcC': 'I',
  '\xcd': 'I',
  '\xce': 'I',
  '\xcf': 'I',
  '\xeC': 'i',
  '\xed': 'i',
  '\xee': 'i',
  '\xef': 'i',
  '\xd1': 'N',
  '\xf1': 'n',
  '\xd2': 'O',
  '\xd3': 'O',
  '\xd4': 'O',
  '\xd5': 'O',
  '\xd6': 'O',
  '\xd8': 'O',
  '\xf2': 'o',
  '\xf3': 'o',
  '\xf4': 'o',
  '\xf5': 'o',
  '\xf6': 'o',
  '\xf8': 'o',
  '\xd9': 'U',
  '\xda': 'U',
  '\xdb': 'U',
  '\xdc': 'U',
  '\xf9': 'u',
  '\xfa': 'u',
  '\xfb': 'u',
  '\xfc': 'u',
  '\xdd': 'Y',
  '\xfd': 'y',
  '\xff': 'y',
  '\xc6': 'Ae',
  '\xe6': 'ae',
  '\xde': 'Th',
  '\xfe': 'th',
  '\xdf': 'ss',
}

"""
Convert first letter of string to lowercase
"""
def lower_case_first_letter(string):
  return string[0:1].lower() + string[1:]

"""
Convert first letter of string to uppercase
"""
def upper_case_first_letter(string):
  return string[0:1].upper() + string[1:]

"""
Remove accents from Latin letters

Déjà Vu => Deja Vu
"""
def deburr(string):
  deburred = ""

  for char in string:
    if char in DEBURRED_LETTERS:
      deburred += DEBURRED_LETTERS[char]
    else:
      deburred += char

  return deburred

"""
Convert to pascal case

hello_world => helloWorld
"""
def convert_to_camel_case(string):
  def convert_by_group(match):
    def convert_section(match):
      string = match.group(1)
      string = string.lower()
      string = upper_case_first_letter(string)
      return string
    string = match.group(1)
    string = re.sub('([A-Z]+|[A-Z]?[a-z]+)([_-]+|$)', convert_section, string)
    string = lower_case_first_letter(string)
    return string

  string = deburr(string)
  string = re.sub('([A-Za-z0-9_-]+)', convert_by_group, string)
  return string

"""
Convert to pascal case

hello_world => hello-world
"""
def convert_to_kebab_case(string):
  def convert_by_group(match):
    string = match.group(1)
    string = re.sub('([0-9A-Za-z]+)([ _]+)([0-9A-Za-z]+)', r'\1-\3', string)
    string = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', string)
    string = re.sub('([a-z0-9])([A-Z])', r'\1-\2', string)
    return string.lower()

  string = deburr(string)
  string = re.sub('([A-Za-z0-9_-]+)', convert_by_group, string)
  return string

"""
Convert to pascal case

hello_world => HelloWorld
"""
def convert_to_pascal_case(string):
  def convert_by_group(match):
    def convert_section(match):
      string = match.group(1)
      string = string.lower()
      string = upper_case_first_letter(string)
      return string

    string = match.group(1)
    string = re.sub('([A-Z]?[a-z]+)([_-]+|$)', convert_section, string)
    return upper_case_first_letter(string)

  string = deburr(string)
  string = re.sub('([A-Za-z0-9_-]+)', convert_by_group, string)
  return string

"""
Convert to snake case

HelloWorld => hello_world
"""
def convert_to_snake_case(string):
  def convert_by_group(match):
    string = match.group(1)
    string = re.sub('([0-9A-Za-z]+)([ -]+)([0-9A-Za-z]+)', r'\1_\3', string)
    string = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string)
    string = re.sub('([a-z0-9])([A-Z])', r'\1_\2', string)
    return string.lower()

  string = deburr(string)
  string = re.sub('([A-Za-z0-9_-]+)', convert_by_group, string)
  return string
