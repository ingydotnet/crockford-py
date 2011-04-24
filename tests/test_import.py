from package.unittest import *

class TestImport(TestCase):
    def test_import(self):
        import crockford

        self.assertTrue(True, 'crockford module imported cleanly')

if __name__ == '__main__':
    main()
