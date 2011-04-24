from package.unittest import *

import crockford

class TestFunctions(TestCase):
    def test_encode(self):
        self.assertEquals(
            crockford.b32encode('foo'),
            'CSQPY',
            'b32encode works'
        )

    def test_decode(self):
        self.assertEquals(
            crockford.b32decode('CSQPY'),
            'foo',
            'b32decode works'
        )

if __name__ == '__main__':
    main()
