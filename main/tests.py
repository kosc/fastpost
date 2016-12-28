from django.contrib.auth.models import User
from django.test import TestCase
from main.models import Post


class PostTestCase(TestCase):

    def setUp(self):
        pass

    def test_create_new_post(self):
        response = self.client.get('/newpost')
        self.assertEqual(response.status_code, 200)
        test_post_data = {
                    'title': 'Test post title',
                    'content': 'Test post content',
                    'author': 'register_user_test'
                }
        response = self.client.post('/newpost', test_post_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test post title")


class AuthTestCase(TestCase):

    def setUp(self):
        pass

    def test_register(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Register')
        response = self.client.get('/register')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Username')
        self.assertContains(response, 'Password')
        self.assertContains(response, 'Password confirmation')
        test_user_data = {
                    'username': 'register_test_user',
                    'password1': 'T3stP4ssw0rd',
                    'password2': 'T3stP4ssw0rd',
                }
        response = self.client.post('/register', test_user_data)
        self.assertEqual(response.status_code, 302)
        user = User.objects.get(username='register_test_user')
        assert(isinstance(user, User))
        assert(user.check_password('T3stP4ssw0rd'))

    def test_login(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Username')
        self.assertContains(response, 'Password')
        test_user_data = {
                'username': 'register_test_user',
                'password': 'T3stP4ssw0rd',
            }
        response = self.client.post('/login', test_user_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "register_test_user")

    def test_logout(self):
        register_user_data = {
                'username': 'register_test_user',
                'password1': 'T3stP4ssw0rd',
                'password2': 'T3stP4ssw0rd',
            }
        response = self.client.post('/register', register_user_data)
        login_user_data = {
                'username': 'register_test_user',
                'password': 'T3stP4ssw0rd',
            }
        response = self.client.post('/login', login_user_data, follow=True)
        self.assertContains(response, "Logout")
        response = self.client.get('/logout', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Login")
