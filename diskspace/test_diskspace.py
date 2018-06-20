import diskspace
import unittest
import random
import contextlib
import sys

class test_subprocess_check_output(unittest.TestCase):
    def test_subprocess_check(self):
        command = 'du -d 1'
        message = diskspace.subprocess_check_output(command)
        self.assertIsInstance(message, str)

class test_bytes_to_readable(unittest.TestCase):

    def test_blocks_has_something(self):
        Anumber = random.randint(1,6)
        blocks = Anumber
        bytes_size = diskspace.bytes_to_readable(blocks)
        self.assertNotEqual('0.00B', bytes_size)

    def test_blocks_empty(self):
        blocks = 0
        bytes_size = diskspace.bytes_to_readable(blocks)
        self.assertEqual('0.00B', bytes_size)

    def test_blocks_type(self):
        blocks = 0
        bytes_size = diskspace.bytes_to_readable(blocks)
        self.assertIsInstance(bytes_size, str)

    def test_blocks_label_B(self):
        blocks = 1
        bytes_size = diskspace.bytes_to_readable(blocks)
        self.assertEqual('B', bytes_size[-1:])

    def test_blocks_label_KB(self):
        blocks = 1000
        bytes_size = diskspace.bytes_to_readable(blocks)
        self.assertEqual('Kb', bytes_size[-2:])

    def test_blocks_label_MB(self):
        blocks = 1000*1000
        bytes_size = diskspace.bytes_to_readable(blocks)
        self.assertEqual('Mb', bytes_size[-2:])

    def test_blocks_label_GB(self):
        blocks = 1000*1000*1000
        bytes_size = diskspace.bytes_to_readable(blocks)
        self.assertEqual('Gb', bytes_size[-2:])

    def test_blocks_label_TB(self):
        blocks = 1000*1000*1000*1000
        bytes_size = diskspace.bytes_to_readable(blocks)
        self.assertEqual('Tb', bytes_size[-2:])

class test_print_tree(unittest.TestCase):

    def test_full_percentage(self):
        file_tree_node = {'print_size': '2.00Kb', 'children': [], 'size': 4}
        total_size = 4
        percentage = diskspace.calc_percentage(file_tree_node, total_size)
        self.assertEqual(100, percentage)

    def test_no_percentage(self):
        file_tree_node = {'print_size': '2.00Kb', 'children': [], 'size': 0}
        total_size = 100
        percentage = diskspace.calc_percentage(file_tree_node, total_size)
        self.assertEqual(0, percentage)

    def test_rand_percentage(self):
        file_tree_node = {'print_size': '2.00Kb', 'children': [], 'size': 7}
        total_size = 25
        percentage = diskspace.calc_percentage(file_tree_node, total_size)
        self.assertEqual(28, percentage)

    """
    def test_return_statment(self):
        file_tree = "{'/home/user/Docs/folder00/folder01/folder02/testfile.py': {'print_size': '2.00Kb', 'children': [], 'size': 4}}"
        file_tree_node =  {'print_size': '2.00Kb', 'children': [], 'size': 4}
        path = "/home/user/Docs/folder00/folder01/folder02/testfile.py"
        largest_size  = 6
        total_size = 4
        depth = 0
        tree = diskspace.print_tree(file_tree, file_tree_node, path, largest_size, total_size)
        self.assertEqual(None, tree)
        """
    pass

class test_show_space_list(unittest.TestCase):
    pass


suite = unittest.TestLoader().loadTestsFromTestCase(test_subprocess_check_output)
unittest.TextTestRunner(verbosity=2).run(suite)
suite = unittest.TestLoader().loadTestsFromTestCase(test_bytes_to_readable)
unittest.TextTestRunner(verbosity=2).run(suite)
suite = unittest.TestLoader().loadTestsFromTestCase(test_print_tree)
unittest.TextTestRunner(verbosity=2).run(suite)
suite = unittest.TestLoader().loadTestsFromTestCase(test_show_space_list)
unittest.TextTestRunner(verbosity=2).run(suite)
