import unittest
from typing import Iterable

from loginvalidate import is_login_valid_python_lambdas


class TestValidation(unittest.TestCase):

    def _validate_logins(self, logins: Iterable[str], is_true) -> None:
        asserting = [self.assertFalse, self.assertTrue][is_true]
        for word in logins:
            asserting(is_login_valid_python_lambdas(word))

    def test_invalid_end(self):
        self._validate_logins(
            (
                'ads1v-fsaFsa.ffadkf.',
                'ads1v-fsaFsa.ffadkf-'
            ),
            False
        )

    def test_invalid_symbols(self):
        self._validate_logins(
            (
                'ads1v-fs?Fsa.ffadkf',
                'ads1v-fs!Fsa.ffadkf',
                'ads1v-fs#Fsa.ffadkf',
                'ads1v-fs$Fsa.ffadkf',
                'ads1v-fs\Fsa.ffadkf',
            ),
            False
        )

    def test_invalid_start(self):
        self._validate_logins(
            (
                '1',
                '2ds1v-fsFsa.ffadkf',
                '.ds1v-fsFsa.ffadkf',
                '-ds1v-fsFsa.ffadkf',
            ),
            False
        )

    def test_invalid_len(self):
        self._validate_logins(
            (
                'ads1v-fsaFsa.ffadkfBq',
                'ads1v-fsaFsa.ffadkfAZasdf'
            ),
            False
        )

    def test_is_valid(self):
        invalid_logins = (
            'Zds1v-fsaFsa.ffadkf',
            'fdasfdasfjASJDKFJfd',
            'AfdsafasdfF',
            'a',
            'z2',
            '',
            'ABC2',
            'Z.-a'
        )

        self._validate_logins(invalid_logins, True)
