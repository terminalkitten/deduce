import unittest

from deduce import utilcls


class TestUtilClsMethods(unittest.TestCase):
    def test_annotation_to_test(self):
        annotation = utilcls.Annotation(0, 10, "PERSOON", "Jan Jansen")
        self.assertEqual("<PERSOON Jan Jansen>", annotation.to_text())

    def test_replace_tag(self):
        annotation = utilcls.Annotation(0, 10, "PERSOON", "Jan Jansen")
        expected = utilcls.Annotation(0, 10, "BEBOP", "Jan Jansen")
        retrieved = utilcls.replace_tag(annotation, "BEBOP")
        self.assertEqual(expected, retrieved)

if __name__ == "__main__":
    unittest.main()
