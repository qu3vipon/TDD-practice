from django.utils.html import escape

from .base import FunctionalTest
from lists.forms import DUPLICATE_ITEM_ERROR, EMPTY_LIST_ERROR


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, EMPTY_LIST_ERROR)

        self.get_item_input_box().send_keys('우유 사기\n')
        self.check_for_row_in_list_table('1: 우유 사기')

        self.get_item_input_box().send_keys('\n')

        self.check_for_row_in_list_table('1: 우유 사기')

        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, EMPTY_LIST_ERROR)

        self.get_item_input_box().send_keys('tea 만들기\n')
        self.check_for_row_in_list_table('1: 우유 사기')
        self.check_for_row_in_list_table('2: tea 만들기')

    def test_cannot_add_duplicate_items(self):
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('콜라 사기\n')
        self.check_for_row_in_list_table('1: 콜라 사기')

        self.get_item_input_box().send_keys('콜라 사기\n')
        self.check_for_row_in_list_table('1: 콜라 사기')

        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, escape(DUPLICATE_ITEM_ERROR))
