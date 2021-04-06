import pytest

from appiumTest.WebBase.app import App


class TestAddDeleteUser:
    def setup_class(self):
        self.app = App()
        self.app.start_app()
        self.contact_list_page = self.app.goto_main() \
            .go_to_contact_list_page()

    def teardown_class(self):
        self.app.stop_app()

    @pytest.mark.parametrize("username, mobileid", [("wenshue", 12011312130),
                                                    ("wenshuf",14570514567)])
    def test_add_user(self, username, mobileid):
        self.add_member_page = self.contact_list_page.move_to_add_memeber_page()
        self.add_member_page.add_member_info_manually(username, mobileid, keep_add=False)
        self.add_member_page.back_to_contact_list_page()
        notification = self.add_member_page.get_toast_notification()
        assert notification == "添加成功", f"Fail to add user {username}"

    def test_delete_user(self):
        username = "wenshua"
        user_info_page = self.contact_list_page.move_to_user_info_page(username)
        user_info_page.driver.save_screenshot('./temp.png')
        user_info_page.move_to_user_action_page().move_to_edit_user().remove_user()
        result = self.contact_list_page.search_user(username)
        assert not result, f"Fail to remove member {username}"




