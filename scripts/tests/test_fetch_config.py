from pathlib import Path
from typing import Dict
import unittest
from json import loads

from ..fetch_config import main

class TestFetchConfig(unittest.TestCase):
    config = Path(__file__).resolve().parent / 'data/config'
    expected = Path(__file__).resolve().parent / 'data/config/expected'

    def test_main(self):
        out, code = main(self.config / 'good.json')
        self.assertEqual(code, 0)
        expected: Dict
        with (self.expected / 'good.json').open() as f:
            expected = loads(f.read())
        actual: Dict = loads(out)
        self.assertDictEqual(actual, expected)

    def test_main_bad_stable(self):
        out, code = main(self.config / 'bad_stable.json')
        self.assertEqual(code, 2)
        actual: Dict = loads(out)
        self.assertDictEqual(actual, {})

    def test_main_missing_latest(self):
        out, code = main(self.config / 'missing_latest.json')
        self.assertEqual(code, 2)
        actual: Dict = loads(out)
        self.assertDictEqual(actual, {})

    def test_main_missing_releases(self):
        out, code = main(self.config / 'missing_releases.json')
        self.assertEqual(code, 2)
        actual: Dict = loads(out)
        self.assertDictEqual(actual, {})

    def test_main_missing_repo(self):
        out, code = main(self.config / 'missing_repo.json')
        self.assertEqual(code, 2)
        actual: Dict = loads(out)
        self.assertDictEqual(actual, {})

    def test_main_missing_stable(self):
        out, code = main(self.config / 'missing_stable.json')
        self.assertEqual(code, 2)
        actual: Dict = loads(out)
        self.assertDictEqual(actual, {})
