import re, sublime, sublime_plugin
from .lib import strings

CAMEL_CASE = "camel_case"
KEBAB_CASE = "kebab_case"
PASCAL_CASE = "pascal_case"
SNAKE_CASE = "snake_case"

class StringCaseCommand(sublime_plugin.TextCommand):
  def run(self, edit, convet_type = CAMEL_CASE):
    for selection in reversed(self.view.sel()):
      text = self.view.substr(selection)
      if text != "":
        if convet_type == CAMEL_CASE:
          self.view.replace(edit, selection, self.convert_to_camel_case(text))
        elif convet_type == KEBAB_CASE:
          self.view.replace(edit, selection, self.convert_to_kebab_case(text))
        elif convet_type == PASCAL_CASE:
          self.view.replace(edit, selection, self.convert_to_pascal_case(text))
        elif convet_type == SNAKE_CASE:
          self.view.replace(edit, selection, self.convert_to_snake_case(text))

  def convert_to_camel_case(self, string):
    return strings.convert_to_camel_case(string)

  def convert_to_kebab_case(self, string):
    return strings.convert_to_kebab_case(string)

  def convert_to_pascal_case(self, string):
    return strings.convert_to_pascal_case(string)

  def convert_to_snake_case(self, string):
    return strings.convert_to_snake_case(string)
