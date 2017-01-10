import unittest
from dystic import builder


class BuilderTest(unittest.TestCase):
    def test_build_folder(self):
        b = builder.Builder()
        b.build_dir('.')


if __name__ == '__main__':
    unittest.main()
