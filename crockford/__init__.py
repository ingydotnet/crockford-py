"""\
Encode and decode using Douglas Crockford's base32 encoding scheme:

    http://www.crockford.com/wrmg/base32.html

The module uses the base64 module's API for base32 functions:

    base64.b32encode(s)
    base64.b32decode(s[, casefold[, map01]])

See base64 for more info.
"""

__version__ = '0.0.2'

import base64, string

__std2crock = string.maketrans(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567",
    "0123456789ABCDEFGHJKMNPQRSTVWXYZ"
)
__crock2std = string.maketrans(
    "0123456789ABCDEFGHJKMNPQRSTVWXYZ",
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
)

def b32encode(s):
    return base64.b32encode(s).translate(__std2crock, '=')

def b32decode(b32, casefold=None, map01=None):
    # Ensure the manatory padding is correct:
    b32 += '=' * ((8 - len(b32) % 8) % 8)
    return base64.b32decode(b32.translate(__crock2std),
        casefold=casefold, map01=map01)
