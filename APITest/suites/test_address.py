import pytest
import requests

from APITest.WebBase.address_page import AddressPage


class TestAddress:

    def setup_class(self):
        self.addressPage = AddressPage()
        self.user_info = {"name": "zhangSan", "userid": "0001", "department": [1], "mobile": "13800000000"}

    def tear_down(self):
        self.addressPage.delete_user(self.user_info["userid"])

    def test_create_user(self):
        response = self.addressPage.create_user(self.user_info)
        print(response.json())
        assert response.json()["errmsg"] == "created"

    def test_get_user_information(self):
        self.addressPage.create_user(self.user_info)
        response = self.addressPage.get_user_information(self.user_info["userid"])
        assert response.json()["errmsg"] == "ok"
        assert response.json()["name"] == self.user_info["name"]

    @pytest.mark.parametrize('name', ["NewName1", "NewName2"])
    def test_update_user_info(self, name):
        self.addressPage.create_user(self.user_info)
        new_user_info = {"userid": self.user_info["userid"], "name": name}
        response = self.addressPage.modify_user_information(new_user_info)
        print(response.json())
        assert response.json()["errmsg"] == "updated"

    def test_delete_user(self):
        self.addressPage.create_user(self.user_info)
        response = self.addressPage.delete_user(self.user_info["userid"])
        assert response.json()["errmsg"] == "deleted"





