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

"""abydos.distance._softy_cosine.

Soft Cosine similarity & distance
"""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from ._levenshtein import Levenshtein
from ._token_distance import _TokenDistance

__all__ = ['SoftCosine']


class SoftCosine(_TokenDistance):
    """Soft Cosine similarity.

    As described in :cite:`Sidorov:2014`, soft cosine similarity is:
    :math:`sim_{soft cosine}(X, Y) = \frac{\sum_{i}\sum_{j} s_{ij} X_i Y_j}
    {\sqrt{\sum_{i}\sum_{j} s_{ij} X_i X_j}
    \sqrt{\sum_{i}\sum_{j} s_{ij} Y_i Y_j}}`, where :math:`s_{ij}` is the
    similarity of two tokens, by default a function of Levenshtein distance:
    :math:`\frac{1}{1+Levenshtein\_distance(i, j)}.

    .. versionadded:: 0.4.0
    """

    def __init__(self, tokenizer=None, metric=None, sim_method='a', **kwargs):
        """Initialize SoftCosine instance.

        Parameters
        ----------
        tokenizer : _Tokenizer
            A tokenizer instance from the abydos.tokenizer package, defaulting
            to the QGrams tokenizer with q=4
        threshold : float
            The minimum similarity for a pair of tokens to contribute to
            similarity
        metric : _Distance
            A distance instance from the abydos.distance package, defaulting
            to Levenshtein distance
        sim_method : str
            Selects the similarity method from the four given in
            :cite:`Sidorov:2014`:

                - a. :math:`\frac{1}{1+d}`
                - b. :math:`1-\frac{d}{m}`
                - c. :math:`\sqrt{1-\frac{d}{m}}`
                - d. :math:`\Big(1-\frac{d}{m}\Big)

            Where :math:`d` is the distance (Levenshtein by default) and
            :math:`m` is the maximum length of the two tokens. Option `a` is
            default, as suggested by the paper.
        **kwargs
            Arbitrary keyword arguments

        Raises
        ------
        ValueError
            sim_method must be one of 'a', 'b', 'c', or 'd'

        Other Parameters
        ----------------
        qval : int
            The length of each q-gram. Using this parameter and tokenizer=None
            will cause the instance to use the QGram tokenizer with this
            q value.

        .. versionadded:: 0.4.0

        """
        super(SoftCosine, self).__init__(tokenizer, **kwargs)
        self.params['metric'] = metric if metric is not None else Levenshtein()
        if sim_method not in 'abcd':
            raise ValueError("sim_method must be one of 'a', 'b', 'c', or 'd'")
        self.params['sim_method'] = sim_method

    def sim(self, src, tar):
        r"""Return the Soft Cosine similarity of two strings.

        Parameters
        ----------
        src : str
            Source string (or QGrams/Counter objects) for comparison
        tar : str
            Target string (or QGrams/Counter objects) for comparison

        Returns
        -------
        float
            Fuzzy Cosine similarity

        Examples
        --------
        >>> cmp = SoftCosine()
        >>> cmp.sim('cat', 'hat')
        0.5
        >>> cmp.sim('Niall', 'Neil')
        0.3651483716701107
        >>> cmp.sim('aluminum', 'Catalan')
        0.11785113019775793
        >>> cmp.sim('ATCG', 'TAGC')
        0.0

        """
        if src == tar:
            return 1.0
        if not src or not tar:
            return 0.0

        self.tokenize(src, tar)

        similarity = {
            'a': lambda src, tar: 1
            / (1 + self.params['metric'].dist_abs(src, tar)),
            'b': lambda src, tar: 1
            - (
                self.params['metric'].dist_abs(src, tar)
                / max(len(src), len(tar))
            ),
            'c': lambda src, tar: (
                1
                - (
                    self.params['metric'].dist_abs(src, tar)
                    / max(len(src), len(tar))
                )
            )
            ** 0.5,
            'd': lambda src, tar: (
                1
                - (
                    self.params['metric'].dist_abs(src, tar)
                    / max(len(src), len(tar))
                )
            )
            ** 2,
        }

        nom = 0
        denom_left = 0
        denom_right = 0

        for src in self._src_tokens.keys():
            for tar in self._tar_tokens.keys():
                nom += (
                    self._src_tokens[src]
                    * self._tar_tokens[tar]
                    * similarity[self.params['sim_method']](src, tar)
                )

        for src in self._src_tokens.keys():
            for tar in self._src_tokens.keys():
                denom_left += (
                    self._src_tokens[src]
                    * self._src_tokens[tar]
                    * similarity[self.params['sim_method']](src, tar)
                )

        for src in self._tar_tokens.keys():
            for tar in self._tar_tokens.keys():
                denom_right += (
                    self._tar_tokens[src]
                    * self._tar_tokens[tar]
                    * similarity[self.params['sim_method']](src, tar)
                )

        return nom / (denom_left ** 0.5 * denom_right ** 0.5)


if __name__ == '__main__':
    import doctest

    doctest.testmod()