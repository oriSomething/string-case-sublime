import unittest
import strings


TEST_STRINGS = [
  'foøBar',
  'fooBar',
  'FooBar',
  'foo-bar',
  'foo_bar',
]

class TestStrings(unittest.TestCase):
  def test_deburr(self):
    # deburr strings
    self.assertEqual(strings.deburr("Déjà Vu"), "Deja Vu", "succeed conversion")

    # should not deburr latin-1 mathematical operators
    self.assertEqual(strings.deburr("\xd7"), "\xd7", "excluded characters 1/2")
    self.assertEqual(strings.deburr("\xf7"), "\xf7", "excluded characters 2/2")

  def test_convert_to_camel_case(self):
    for test_string in TEST_STRINGS:
      self.assertEqual(strings.convert_to_camel_case(test_string), 'fooBar')
    self.assertEqual(strings.convert_to_camel_case('fooBAR'), 'fooBAR')
    self.assertEqual(strings.convert_to_camel_case('FOO_BAR'), 'fooBar')
    self.assertEqual(strings.convert_to_camel_case('FooBarFooBar'), 'fooBarFooBar')
    self.assertEqual(strings.convert_to_camel_case('foo_bar foo_bar'), 'fooBar fooBar')
    self.assertEqual(strings.convert_to_camel_case('foo_bar_foo_bar'), 'fooBarFooBar')

  def test_convert_to_kebab_case(self):
    for test_string in TEST_STRINGS:
      self.assertEqual(strings.convert_to_kebab_case(test_string), 'foo-bar')

  def test_convert_to_pascal_case(self):
    self.assertEqual(strings.convert_to_pascal_case('foo_bar_foo_bar'), 'FooBarFooBar')
    self.assertEqual(strings.convert_to_pascal_case('foo_bar foo_bar'), 'FooBar FooBar')
    for test_string in TEST_STRINGS:
      self.assertEqual(strings.convert_to_pascal_case(test_string), 'FooBar')

  def test_convert_to_snake_case(self):
    for test_string in TEST_STRINGS:
      self.assertEqual(strings.convert_to_snake_case(test_string), 'foo_bar')


if __name__ == '__main__':
    unittest.main()
