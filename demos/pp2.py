import unittest
import requests


class IntegerArithmeticTestCase (unittest.TestCase):
    def setUp(self):
        print("setup func")

    def tearDown(self):
        print("teardown func")

    def testDivideInteger(self):
        res = 9//4
        hope = 2
        self.assertEqual(res, hope, msg="整除结果为整数")

    @unittest.skip('skip testIn')
    def testIn(self):
        subst = "two"
        st = {"hello", "world", "one", "two"}
        self.assertIn(subst, st)
        # self.assertNotIn(subst, st)

    def testTrueOrFalse(self):
        a = True
        b = False
        self.assertTrue(a)
        self.assertFalse(a and b)

    def testIs(self):
        a = 10
        b = a
        c = 10
        self.assertIs(a, b)
        # self.assertIsNot(b, a)

    def testKuaiDi(self):
        h = {
            "Host": "www.kuaidi.com",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3620.400",
            "Referer": "http://www.kuaidi.com/",
        }
        url = \
   "http://www.kuaidi.com/index-ajaxselectcourierinfo-552027047111994-huitongkuaidi-XCAO1605165158370.html"
        r = requests.post(url, headers=h)
        res = r.json()
        data = res['data']
        # print(r.json())
        # print("快递单号：{}".format(res['nu']))
        # print("company：{}".format(res['company']))
        # print("最新状态：{}".format(data[0]['context']))
        self.assertIn("签收", data[0]['context'])


def suite():
    suite = unittest.TestSuite()
    # suite.addTest(IntegerArithmeticTestCase('testDivideInteger'))
    #     # suite.addTest(IntegerArithmeticTestCase('testKuaiDi'))
    #     # suite.addTest(IntegerArithmeticTestCase('testIn'))
    suite.addTest (IntegerArithmeticTestCase('testIs'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
    # unittest.main()
