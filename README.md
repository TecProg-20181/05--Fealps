Disk Space Command
==================

Show how much each folder and file ocuppies in relation to the searched
directory.

Install
=======

```python
python setup.py install
```

Usage
=====

```
usage: diskspace.py [-h] [-o {desc,asc}] [-s HIDE] [-a | -d DEPTH] [-t] [DIR]

Analizes and reports the disk usage per folder

positional arguments:
  DIR                   Directory to be analized

optional arguments:
  -h, --help            show this help message and exit
  -o {desc,asc}, --order {desc,asc}
                        The file order inside each folder
  -s HIDE, --hide HIDE  Hides all files that have a percentage lower than this
                        value
  -a, --all             Shows the full tree
  -d DEPTH, --depth DEPTH
                        Specifies the folder maximum depth to be analyzed
  -t, --tree-view       Display the result in a tree mode
```
testing
=====
```
To run the test_diskspace.py open the folder where test_diskspace is in using the
terminal and run the following command:

          python -m unittest  test_diskspace

```
