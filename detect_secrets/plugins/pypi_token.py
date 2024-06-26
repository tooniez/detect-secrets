"""
This plugin searches for PyPI tokens
"""
import re

from detect_secrets.plugins.base import RegexBasedDetector


class PypiTokenDetector(RegexBasedDetector):
    """Scans for PyPI tokens."""
    secret_type = 'PyPI Token'

    denylist = [
        # refs https://warehouse.pypa.io/development/token-scanning.html
        # pypi.org token
        re.compile(r'pypi-AgEIcHlwaS5vcmc[A-Za-z0-9-_]{70,}'),

        # test.pypi.org token
        re.compile(r'pypi-AgENdGVzdC5weXBpLm9yZw[A-Za-z0-9-_]{70,}'),
    ]
