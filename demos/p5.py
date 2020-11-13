import unittest
import requests


class IntegerArithmeticTestCase (unittest.TestCase):
    def setUp(self):
        print("setup func")

    def tearDown(self):
        print("teardown func")

    def testAdd(self):  # test method names begin with 'test'
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)

    def testMultiply(self):
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)

    def testMinus(self):
        res = 9-3
        hope = 6
        self.assertEqual(res, hope)

    def testDivide(self):
        res = 9/3
        hope = 3
        self.assertEqual(res, hope)

    def testDivideInteger(self):
        res = 9//4
        hope = 2
        self.assertEqual(res, hope, msg="整除结果为整数")

    def testIn(self):
        subst = "two13"
        st = {"hello", "world", "one", "two"}
        # self.assertIn(subst, st)
        self.assertNotIn(subst, st)

    def testTrueOrFalse(self):
        a = True
        b = False
        self.assertTrue(a)
        self.assertFalse(a and b)

    def testNone(self):
        a = []
        b = None
        self.assertIsNotNone(a)
        self.assertIsNone(b)
   "http://www.kuaidi.com/index-ajaxselectcourierinfo-552027047111994-huitongkuaidi-XCAO1605165158370.html"
        r = requests.post(url, headers=h)
        res = r.json()
        data = res['data']
        # print(r.json())
        # print("快递单号：{}".format(result['nu']))
        # print("company：{}".format(result['company']))
        # print("最新状态：{}".format(data[0]['context']))
        self.assertIn("签收", data[0]['context'])


if __name__ == '__main__':
    unittest.main()
