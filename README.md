# Description 
Simple command line file hex viewer.

## Usage
```
$ hexy -f setup.py -c 16
```

```
22 22 22 0D 0A 54 68 69 | 73 20 6D 6F 64 75 6C 65  |  """  This module
20 64 65 66 69 6E 65 73 | 20 74 68 65 20 61 74 74  |   defines the att
72 69 62 75 74 65 73 20 | 6F 66 20 74 68 65 0D 0A  |  ributes of the
50 79 50 49 20 70 61 63 | 6B 61 67 65 20 66 6F 72  |  PyPI package for
20 74 68 65 20 6D 62 65 | 64 20 53 44 4B 20 74 65  |   the mbed SDK te
73 74 20 73 75 69 74 65 | 0D 0A 22 22 22 0D 0A 0D  |  st suite  """
0A 22 22 22 0D 0A 6D 62 | 65 64 20 53 44 4B 0D 0A  |   """  mbed SDK

...

20 20 7D 2C 0D 0A 20 20 | 20 20 20 20 69 6E 73 74  |    },        inst
61 6C 6C 5F 72 65 71 75 | 69 72 65 73 3D 5B 22 63  |  all_requires=["c
6F 6C 6F 72 61 6D 61 3E | 3D 30 2E 33 2C 3C 30 2E  |  olorama>=0.3,<0.
34 22 5D 29 0D 0A       |                          |  4"])
```
