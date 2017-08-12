from django.contrib.auth.models import User
from django.test import TestCase

from captcha.models import CaptchaStore


class PostTestCase(TestCase):

    @classmethod
    def setUpTestData(self):
        super(PostTestCase, self).setUpTestData()
        self.test_user = User()
        self.test_user.username = "test_user"
        self.test_user.set_password("T3stP4ssw0rd")
        self.test_user.save()

    def test_create_new_post(self):
        user = User.objects.get(username='test_user')
        self.client.login(username="test_user", password="T3stP4ssw0rd")
        # add post
        response = self.client.get('/newpost')
        self.assertEqual(response.status_code, 200)
        test_post_data = {
                    'title': 'Test post title',
                    'content': 'Test post content',
                    'author': user,
                }
        response = self.client.post('/newpost', test_post_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test post title")
        self.assertContains(response, "Test post content")
        user.delete()


class AuthTestCase(TestCase):

    def setUp(self):
        pass

    def test_register(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Register')
        captcha_count = CaptchaStore.objects.count()
        self.failUnlessEqual(captcha_count, 0)
        response = self.client.get('/register')
        self.assertEqual(response.status_code, 200)
        captcha_count = CaptchaStore.objects.count()
        self.failUnlessEqual(captcha_count, 1)
        self.assertContains(response, 'Username')
        self.assertContains(response, 'Password')
        self.assertContains(response, 'Password confirmation')
        self.assertContains(response, 'Captcha')
        captcha = CaptchaStore.objects.all()[0]
        test_user_data = {
                    'username': 'register_test_user',
                    'password1': 'T3stP4ssw0rd',
                    'password2': 'T3stP4ssw0rd',
                    'captcha_0': captcha.hashkey,
                    'captcha_1': captcha.response,
                }
        response = self.client.post('/register', test_user_data)
        self.assertEqual(response.status_code, 302)
        user = User.objects.get(username='register_test_user')
        self.assertTrue(isinstance(user, User))
        self.assertTrue(user.check_password('T3stP4ssw0rd'))

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
        self.client.get('/register')
        captcha = CaptchaStore.objects.all()[0]
        register_user_data = {
                'username': 'register_test_user',
                'password1': 'T3stP4ssw0rd',
                'password2': 'T3stP4ssw0rd',
                'captcha_0': captcha.hashkey,
                'captcha_1': captcha.response,
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


class RegressionTestCase(TestCase):

    @classmethod
    def setUpTestData(self):
        super(RegressionTestCase, self).setUpTestData()
        self.test_user = User()
        self.test_user.username = "test_user"
        self.test_user.set_password("T3stP4ssw0rd")
        self.test_user.save()

    def test_duplicate_slugs(self):
        self.client.login(username="test_user", password="T3stP4ssw0rd")
        first_post_data = {
                'title': 'Test title',
                'content': 'First post content',
            }
        second_post_data = {
                'title': 'Test title',
                'content': 'Second post content',
            }
        response = self.client.post('/newpost', first_post_data, follow=True)
        self.assertContains(response, "First")
        response = self.client.post('/newpost', second_post_data, follow=True)
        self.assertContains(response, "Second")
