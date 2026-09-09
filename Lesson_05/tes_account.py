import unittest

from Lesson_05.account import *

class TestAccount(unittest.TestCase):
    def test_strip_space(self):
        self.assertEqual(clean_name(" aIsic"), "Aisic")

    def test_capitalize(self):
        self.assertEqual(clean_name("sveta"), "Sveta")

    def test_username_from_first_last(self):
        self.assertEqual(make_username("Sveta", "Sveta"), "sveta_sveta")

    def test_valid_email(self):
        self.assertTrue(is_valid_email("aisix123@gmail.com"))

    def test_invalid_email(self):
        self.assertFalse(is_valid_email("aisix123.vhkk.zr"))
        self.assertFalse(is_valid_email("aisix123@vhkk"))

    def test_valid_email_secure(self):
        self.assertTrue(is_valid_email_secure("aisic123@gmail.com"))

    def test_invalid_email_secure(self):
        self.assertFalse(is_valid_email_secure("aisic123@as.d"))

    def test_invalid_email_without_at_secure(self):
        self.assertFalse(is_valid_email_secure("aisic123.fv.hul"))

    def test_invalid_email_without_domain_secure(self):
        self.assertFalse(is_valid_email_secure("aisic123@"))

    def test_invalid_email_without_username_secure(self):
        self.assertFalse(is_valid_email_secure("@gmail.com"))

    def test_invalid_email_without_dot_secure(self):
        self.assertFalse(is_valid_email_secure("@gmailcom"))


class TestUserProfile(unittest.TestCase):


    def setUp(self):
        self.user = {
            "name": "Aisic",
            "email": "aisix26@gmail.com",
            "role": ["user"],
        }

    def test_profile_has_name(self):
        self.assertEqual(self.user["name"], "Aisic")


    def test_valid_email(self):
        self.assertTrue(is_valid_email_secure(self.user["email"]))

    def test_add_role(self):
        self.user["role"].append("admin")
        self.assertIn("admin", self.user["role"])
        self.assertEqual(len(self.user["role"]), 2)

    def test_check_length_role(self):
        self.assertEqual(len(self.user["role"]), 1)


class TestGetInitial(unittest.TestCase):
    def test_get_normal_initials(self):
        self.assertEqual(get_initials("Aisic Jung"), "A.J.")

    def test_str_empty_with_raise_exception(self):
        with self.assertRaises(ValueError):
            get_initials("  ")

    #def test_text_limit(self):
        #self.assertEqual(cut_length("text", 10),"text****")

    def test_text_limit(self):
        self.assertEqual(cut_length("text is not empty", 10),"text is no****")







