# -*- coding: utf-8 -*-

# Copyright 2018 by Christopher C. Little.
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

"""abydos.distance._probabilistic_symmetric_chi_squared.

Probabilistic Symmetric Chi-Squared distance
"""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from ._token_distance import _TokenDistance

__all__ = ['ProbabilisticSymmetricChiSquared']


class ProbabilisticSymmetricChiSquared(_TokenDistance):
    r"""Probabilistic Symmetric Chi-Squared distance.

    For two multisets X and Y drawn from an alphabet S, Probabilistic Symmetric Chi-Squared distance
    :cite:`CITATION` is

        .. math::

            sim_{ProbabilisticSymmetricChiSquared}(X, Y) =

    .. versionadded:: 0.4.0
    """

    def __init__(
        self,
        tokenizer=None,
        **kwargs
    ):
        """Initialize ProbabilisticSymmetricChiSquared instance.

        Parameters
        ----------
        tokenizer : _Tokenizer
            A tokenizer instance from the :py:mod:`abydos.tokenizer` package
        **kwargs
            Arbitrary keyword arguments

        Other Parameters
        ----------------
        qval : int
            The length of each q-gram. Using this parameter and tokenizer=None
            will cause the instance to use the QGram tokenizer with this
            q value.


        .. versionadded:: 0.4.0

        """
        super(ProbabilisticSymmetricChiSquared, self).__init__(
            tokenizer=tokenizer,
            **kwargs
        )

    def sim(self, src, tar):
        """Return the Probabilistic Symmetric Chi-Squared distance of two strings.

        Parameters
        ----------
        src : str
            Source string (or QGrams/Counter objects) for comparison
        tar : str
            Target string (or QGrams/Counter objects) for comparison

        Returns
        -------
        float
            Probabilistic Symmetric Chi-Squared distance

        Examples
        --------
        >>> cmp = ProbabilisticSymmetricChiSquared()
        >>> cmp.sim('cat', 'hat')
        0.0
        >>> cmp.sim('Niall', 'Neil')
        0.0
        >>> cmp.sim('aluminum', 'Catalan')
        0.0
        >>> cmp.sim('ATCG', 'TAGC')
        0.0


        .. versionadded:: 0.4.0

        """
        self.tokenize(src, tar)

        alphabet = self._total().keys()

        return 0.0


if __name__ == '__main__':
    import doctest

    doctest.testmod()