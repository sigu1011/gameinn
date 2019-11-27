import os
import gameinn
import unittest
import tempfile
from gameinn.script.db import InitDB


class TestGameinn(unittest.TestCase):

    def setUp(self):
        self.db_fd, gameinn.DATABASE = tempfile.mkstemp()
        self.app = gameinn.app.test_client()
        InitDB().run()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(gameinn.DATABASE)

    def create_user(self, username, password):
        return self.app.post('/users', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_0_sing_up(self):
        rv = self.create_user('test', 'pass')
        assert 'New user registration is complete. Please sign in.'.encode() in rv.data

        rv = self.create_user('test', 'test')
        assert 'The username already exists.'.encode() in rv.data
        rv = self.create_user('', 'test')
        assert 'The username you have entered is invalid.'.encode() in rv.data
        rv = self.create_user('test', '')
        assert 'The password you have entered is invalid.'.encode() in rv.data
        rv = self.create_user('', '')
        assert 'The username you have entered is invalid.'.encode() in rv.data

    def test_1_login_logout(self):
        self.create_user('test', 'pass')
        rv = self.login('test', 'pass')
        print(rv)
        assert 'Signed in.'.encode() in rv.data
        rv = self.logout()
        assert 'Signed out'.encode() in rv.data

        rv = self.login('', 'pass')
        assert 'The username you have entered is invalid.'.encode() in rv.data
        rv = self.login('test', '')
        assert 'The password you have entered is invalid.'.encode() in rv.data

        rv = self.login('test', 'password')
        assert 'The password you have entered is incorrect.'.encode() in rv.data


if __name__ == '__main__':
    unittest.main()
