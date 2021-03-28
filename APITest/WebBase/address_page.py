from APITest.WebBase.web_base import WebBase


class AddressPage(WebBase):
    def create_user(self, user_info):
        for item in ["userid", "department", "mobile", "name"]:
            if item not in user_info.keys():
                raise KeyError("Mandatory keys are not existed in the body")
        response = self.send("POST",
                             f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}",
                             json=user_info)
        return response

    def get_user_information(self, userid):
        params = {"userid": userid}
        response = self.send("GET", "https://qyapi.weixin.qq.com/cgi-bin/user/get", params=params)
        return response

    def modify_user_information(self, user_info):
        if "userid" not in user_info.keys():
            raise KeyError("userid is a compulsory key in the body")
        response = self.send("POST", "https://qyapi.weixin.qq.com/cgi-bin/user/update", json=user_info)
        return response

    def delete_user(self, userid):
        params = {"userid": userid}
        response = self.send("GET", "https://qyapi.weixin.qq.com/cgi-bin/user/delete", params)
        return response
