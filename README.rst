crockford - Encode and Decode using the Crockford Base32 scheme
---------------------------------------------------------------

Installation
------------

Use::

    > sudo pip install crockford

or::

    > sudo easy install crockford

or::

    > git clone git://github.com/ingydotnet/crockford-py.git
    > cd crockford-py
    > sudo make install

Usage
-----

    import crockford

    base32 = crockford.b32encode(string)
    string = crockford.b32decode(base32)

Authors
-------

* Ingy dot Net <ingy@ingy.net>

Copyright
---------

crockford is Copyright (c) 2011, Ingy dot Net

crockford is licensed under the New BSD License. See the LICENSE file.
