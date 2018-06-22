import diskspace
import unittest
import random
import contextlib
import sys
import argparse
from mock import patch, MagicMock


class test_subprocess_check_output(unittest.TestCase):
    def test_subprocess_check(self):
        """
        test return type
        """
        command = 'du -d 1'
        message = diskspace.subprocess_check_output(command)
        self.assertIsInstance(message, str)

class test_bytes_to_readable(unittest.TestCase):

    def test_blocks_has_something(self):
        """
        test if a random block chunk returns something
        """
        Anumber = random.randint(1,6)
        blocks = Anumber
        bytes_size = diskspace.bytes_to_readable(blocks)
        self.assertNotEqual('0.00B', bytes_size)

    def test_blocks_empty(self):
        """
        test if a 0 sized block chunk returns the apropriate value
        """
        blocks = 0
        bytes_size = diskspace.bytes_to_readable(blocks)
        self.assertEqual('0.00B', bytes_size)

    def test_blocks_type(self):
        """
        test return type
        """
        blocks = 0
        bytes_size = diskspace.bytes_to_readable(blocks)
        self.assertIsInstance(bytes_size, str)

    def test_blocks_label_B(self):
        """
        test if returned label is equal to value passed
        """
        blocks = 1
        bytes_size = diskspace.bytes_to_readable(blocks)
        self.assertEqual('B', bytes_size[-1:])

    def test_blocks_label_KB(self):
        """
        test if returned label is equal to value passed
        """
        blocks = 1000
        bytes_size = diskspace.bytes_to_readable(blocks)
        self.assertEqual('Kb', bytes_size[-2:])

    def test_blocks_label_MB(self):
        """
        test if returned label is equal to value passed
        """
        blocks = 1000*1000
        bytes_size = diskspace.bytes_to_readable(blocks)
        self.assertEqual('Mb', bytes_size[-2:])

    def test_blocks_label_GB(self):
        """
        test if returned label is equal to value passed
        """
        blocks = 1000*1000*1000
        bytes_size = diskspace.bytes_to_readable(blocks)
        self.assertEqual('Gb', bytes_size[-2:])

    def test_blocks_label_TB(self):
        """
        test if returned label is equal to value passed
        """
        blocks = 1000*1000*1000*1000
        bytes_size = diskspace.bytes_to_readable(blocks)
        self.assertEqual('Tb', bytes_size[-2:])

class test_print_tree(unittest.TestCase):

    def test_full_percentage(self):
        """
        test if percentage return full value
        """
        file_tree_node = {'print_size': '2.00Kb', 'children': [], 'size': 4}
        total_size = 4
        percentage = diskspace.calc_percentage(file_tree_node, total_size)
        self.assertEqual(100, percentage)

    def test_no_percentage(self):
        """
        test if percentage return zero value
        """
        file_tree_node = {'print_size': '2.00Kb', 'children': [], 'size': 0}
        total_size = 100
        percentage = diskspace.calc_percentage(file_tree_node, total_size)
        self.assertEqual(0, percentage)

    def test_rand_percentage(self):
        """
        test if percentage return a number value
        """
        file_tree_node = {'print_size': '2.00Kb', 'children': [], 'size': 7}
        total_size = 25
        percentage = diskspace.calc_percentage(file_tree_node, total_size)
        self.assertEqual(28, percentage)
    pass

class test_show_space_list(unittest.TestCase):

    def test_command_line_return_text(self):
        """
        Test if the return string is equal to expected
        """
        path = "~/Directory/folder/folder1/file.py"
        depth = 1
        cmd = diskspace.command_line(path, depth)
        self.assertEqual("du -d 1 ~/Directory/folder/folder1/file.py", cmd)

    def test_command_line_return_type(self):
        """
        test return type of function
        """
        path = "~/"
        depth = 1
        cmd = diskspace.command_line(path, depth)
        self.assertIsInstance(cmd,str)

class test_main_case(unittest.TestCase):
    """
    def test_order(self):
        diskspace.args.directory = MagicMock(return_value = "test_diskspace.py")
        diskspace.args.depth = MagicMock(return_value = 1)
        diskspace.args.order = MagicMock(return_value = "desc")
        diskspace.subprocess_check_output.file_size = MagicMock(value = 12)
        run = diskspace.main()
        self.assertIsInstance(run,str)
        """
    pass

suite = unittest.TestLoader().loadTestsFromTestCase(test_subprocess_check_output)
unittest.TextTestRunner(verbosity=2).run(suite)
suite = unittest.TestLoader().loadTestsFromTestCase(test_bytes_to_readable)
unittest.TextTestRunner(verbosity=2).run(suite)
suite = unittest.TestLoader().loadTestsFromTestCase(test_print_tree)
unittest.TextTestRunner(verbosity=2).run(suite)
suite = unittest.TestLoader().loadTestsFromTestCase(test_show_space_list)
unittest.TextTestRunner(verbosity=2).run(suite)
suite = unittest.TestLoader().loadTestsFromTestCase(test_main_case)
unittest.TextTestRunner(verbosity=2).run(suite)
