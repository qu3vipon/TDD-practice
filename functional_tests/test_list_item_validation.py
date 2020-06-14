from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, '빈 아이템을 등록할 수 없습니다.')

        self.get_item_input_box().send_keys('우유 사기\n')
        self.check_for_row_in_list_table('1: 우유 사기')

        self.get_item_input_box().send_keys('\n')

        self.check_for_row_in_list_table('1: 우유 사기')

        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, '빈 아이템을 등록할 수 없습니다.')

        self.get_item_input_box().send_keys('tea 만들기\n')
        self.check_for_row_in_list_table('1: 우유 사기')
        self.check_for_row_in_list_table('2: tea 만들기')
