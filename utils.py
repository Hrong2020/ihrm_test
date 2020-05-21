# 断言方法
import json


def assert_common(httpcode, success, code, message, response, self):
    # 断言登录的结果
    self.assertEqual(httpcode, response.status_code)  # 断言响应状态码
    self.assertEqual(success, response.json().get("success"))  # 断言success
    self.assertEqual(code, response.json().get("code"))  # 断言code
    self.assertIn(message, response.json().get("message"))  # 断言message


def build_data(filename):
    with open(filename, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)
        result_list = []
        for login_data in jsonData:
            result_list.append(list(login_data.values()))
        # 返回结果
        return result_list


def build_emp_data(filename, name):
    with open(filename,mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)
        emp_data = jsonData.get(name)
        result_list = list()
        result_list.append(tuple(emp_data.values()))
    return result_list


if __name__ == '__main__':
    import app

    filename = app.BASE_DIR + "/data/login_data.json"
    print("路径:", filename)
    build_data(filename)
