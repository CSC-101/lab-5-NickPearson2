import data
import lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_time_add1(self):
        time1 = data.Time(8,30,24)
        time2 = data.Time(8,30,24)
        result = data.Time(17,0,48)
        self.assertEqual(lab5.time_add(time1,time2),result)
    def test_time_add2(self):
        time1 = data.Time(8,30,24)
        time2 = data.Time(8,32,40)
        result = data.Time(17,3,4)
        self.assertEqual(lab5.time_add(time1,time2),result)
    # Part 4
    def test_is_descending1(self):
        list = [9.2,8.7,7.5,6.1,5.8]
        self.assertEqual(lab5.is_descending(list),True)
    def test_is_descending2(self):
        list = [9.2, 8.4, 7.5, 6.1, 10.1]
        self.assertEqual(lab5.is_descending(list), False)

    # Part 5
    def test_largest_between1(self):
        list = [10,4,29,2,25,30,20,24,9,10]
        self.assertEqual(lab5.largest_between(list,2,9),5)
    def test_largest_between2(self):
        list = [10,4,29,2,25,30,20,24,9,10]
        self.assertEqual(lab5.largest_between(list,-5,10),5)
    # Part 6
    def test_furthest_from_origin(self):
        point = data.Point(0,5)
        point2 = data.Point(1, 5)
        point3 = data.Point(10, 5)
        point4 = data.Point(2, 4)
        list = [point,point2,point3,point4]
        self.assertEqual(lab5.furthest_from_origin(list),point3)
    def test_furthest_from_origin2(self):
        point = data.Point(0,2)
        point2 = data.Point(20, 0)
        point3 = data.Point(10, 5)
        point4 = data.Point(2, 4)
        list = [point,point2,point3,point4]
        self.assertEqual(lab5.furthest_from_origin(list),point2)
    def test_furthest_from_origin3(self):
        list = []
        self.assertEqual(lab5.furthest_from_origin(list),None)




if __name__ == '__main__':
    unittest.main()
