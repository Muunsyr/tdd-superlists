from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser =  webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Magenta has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

        # She types "Nag for food" into a text box (Magaenta is a cat.
        # She likes to be annoying.)

# When she hits enter, the page updates, and now the page lists
# "1: Nag for food" as an item in a to-do list

# There is still a text box inviting her to add another item. She
# enters "Eat some of the food given too me" (Magenta is very methodical)

# The page updates again, and now shows both items on her list

# Magenta wonders whether the site will remember her list. Then she sees
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect.

# She visits that URL - her to-do list is still there.

# Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
