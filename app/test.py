import os
import unittest
from PIL import Image
from api import app
from api.helper import conversion_logic

app_path = os.path.dirname(os.path.abspath(__file__))


class AppTestCase(unittest.TestCase):

    def setUp(self):
        # set up test client for main app
        self.app = app.test_client()

    def test_app_running(self):
        # sends HTTP GET request to the application
        response_code = self.app.get('/')
        # assert the status code of the response
        self.assertEqual(response_code.status_code, 200)

    def test_main_page_template(self):
        rv = self.app.get('/')
        # compare some string (from index tempalte) with app route response
        self.assertIn(b'Allowed File Types:', rv.data)
        print("Main page loaded succsessfully")

    def test_upload(self):
        image = Image.open(os.path.join(
            os.path.join(app_path, 'api', 'example_files', 'test.jpg')))
        response = self.app.post("/", data={"image": (image, "test.jpg")})
        self.assertEqual(response.status_code, 200)
        print("File upload is working")

    def test_conversation_logic(self):
        conversion_logic(os.path.join(os.path.join(
            app_path, 'api', 'example_files', 'test.jpg')), '.jpg')
        print("Conversion_logic is working")


if __name__ == '__main__':
    unittest.main()
