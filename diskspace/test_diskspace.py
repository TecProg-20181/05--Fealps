import diskspace
import unittest
import random



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

#def test_print_tree(file_tree, file_tree_node, path, largest_size, total_size, depth=0):
#def test_show_space_list(directory='.', depth=-1, order=True):
#def test_subprocess_check_output():

if __name__ == '__main__':
    unittest.main()
