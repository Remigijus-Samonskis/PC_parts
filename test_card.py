import unittest
from main import PCPart
from parts import PARTS_INFO


class TestParts(unittest.TestCase):
    def setUp(self):
        self.pc_part = PCPart("Intel HD Graphics 4600", 190, 50)
        self.parts_info = PARTS_INFO

    def tearDown(self):
        print("tearDown\n")

    def test_get_name(self):
        result_cart_first = self.pc_part.get_name("Intel HD Graphics 4600")
        self.assertEqual(result_cart_first, [self.parts_info[1]])

        result_cart_second = self.pc_part.get_name("Intel UHD Graphics 630")
        self.assertEqual(result_cart_second, [self.parts_info[2]])

        result_cart_third = self.pc_part.get_name("Intel UHD Graphics 874")
        self.assertEqual(result_cart_third, [self.parts_info[3]])

    def test_get_price(self):
        result_cart_first = self.pc_part.get_price("$190")
        self.assertEqual(result_cart_first, [self.parts_info[1]])

        result_cart_second = self.pc_part.get_price("$105")
        self.assertEqual(result_cart_second, [self.parts_info[2]])

        result_cart_third = self.pc_part.get_price("$2300")
        self.assertEqual(result_cart_third, [self.parts_info[3]])

    def test_get_tdp(self):
        result_cart_first = self.pc_part.get_tdp("50 W")
        self.assertEqual(result_cart_first, [self.parts_info[1]])

        result_cart_second = self.pc_part.get_tdp("65 W")
        self.assertEqual(result_cart_second, [self.parts_info[2]])

        result_cart_third = self.pc_part.get_tdp("280 W")
        self.assertEqual(result_cart_third, [self.parts_info[3]])

    def test_wrong_input(self):
        with self.assertRaises(Exception), PCPart():
            self.pc_part.get_name("Intel HD Graphics 4600")
            self.pc_part.get_price("$190")
            self.pc_part.get_tdp("20 W")


if __name__ == "__main__":
    unittest.main()
