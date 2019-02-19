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

"""abydos.tests.distance.test_distance_clement.

This module contains unit tests for abydos.distance.Clement
"""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

from abydos.distance import Clement


class ClementTestCases(unittest.TestCase):
    """Test Clement functions.

    abydos.distance.Clement
    """

    cmp = Clement()

    def test_clement_sim(self):
        """Test abydos.distance.Clement.sim."""
        # Base cases
        self.assertEqual(self.cmp.sim('', ''), float('nan'))
        self.assertEqual(self.cmp.sim('a', ''), 0.0025510204081632404)
        self.assertEqual(self.cmp.sim('', 'a'), float('nan'))
        self.assertEqual(self.cmp.sim('abc', ''), 0.005102040816326481)
        self.assertEqual(self.cmp.sim('', 'abc'), float('nan'))
        self.assertEqual(self.cmp.sim('abc', 'abc'), 1.0050761421319798)
        self.assertEqual(self.cmp.sim('abcd', 'efgh'), 0.006336616803332366)

        self.assertAlmostEqual(self.cmp.sim('Nigel', 'Niall'), 0.5075797911)
        self.assertAlmostEqual(self.cmp.sim('Niall', 'Nigel'), 0.5075797911)
        self.assertAlmostEqual(self.cmp.sim('Colin', 'Coiln'), 0.5075797911)
        self.assertAlmostEqual(self.cmp.sim('Coiln', 'Colin'), 0.5075797911)
        self.assertAlmostEqual(
            self.cmp.sim('ATCAACGAGT', 'AACGATTAG'), 0.6501817682
        )


if __name__ == '__main__':
    unittest.main()
