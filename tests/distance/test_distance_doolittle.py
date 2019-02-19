# -*- coding: utf-8 -*-

# Copyright 2019 by Christopher C. Little.
# This file is part of Abydos.
#
# Abydos is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Abydos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Abydos. If not, see <http://www.gnu.org/licenses/>.

"""abydos.tests.distance.test_distance_doolittle.

This module contains unit tests for abydos.distance.Doolittle
"""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

from abydos.distance import Doolittle


class DoolittleTestCases(unittest.TestCase):
    """Test Doolittle functions.

    abydos.distance.Doolittle
    """

    cmp = Doolittle()

    def test_doolittle_sim(self):
        """Test abydos.distance.Doolittle.sim."""
        # Base cases
        self.assertEqual(self.cmp.sim('', ''), float('nan'))
        self.assertEqual(self.cmp.sim('a', ''), float('nan'))
        self.assertEqual(self.cmp.sim('', 'a'), float('nan'))
        self.assertEqual(self.cmp.sim('abc', ''), float('nan'))
        self.assertEqual(self.cmp.sim('', 'abc'), float('nan'))
        self.assertEqual(self.cmp.sim('abc', 'abc'), 1.0)
        self.assertEqual(self.cmp.sim('abcd', 'efgh'), 4.1196952743799446e-05)

        self.assertAlmostEqual(self.cmp.sim('Nigel', 'Niall'), 0.2461588279)
        self.assertAlmostEqual(self.cmp.sim('Niall', 'Nigel'), 0.2461588279)
        self.assertAlmostEqual(self.cmp.sim('Colin', 'Coiln'), 0.2461588279)
        self.assertAlmostEqual(self.cmp.sim('Coiln', 'Colin'), 0.2461588279)
        self.assertAlmostEqual(
            self.cmp.sim('ATCAACGAGT', 'AACGATTAG'), 0.439469213
        )


if __name__ == '__main__':
    unittest.main()
