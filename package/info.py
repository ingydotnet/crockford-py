def get():
    info = {}
    info.update(
{ 'author': 'Ingy dot Net',
  'author_email': 'ingy@ingy.net',
  'classifiers': [ 'Development Status :: 2 - Pre-Alpha',
                   'License :: OSI Approved :: BSD License',
                   'Programming Language :: Python',
                   'Intended Audience :: Developers'],
  'description': "Encode and decode using Douglas Crockford's base32 encoding scheme:",
  'long_description': 'crockford - Encode and Decode using the Crockford Base32 scheme\n---------------------------------------------------------------\n\nInstallation\n------------\n\nUse::\n\n    > sudo pip install crockford\n\nor::\n\n    > sudo easy install crockford\n\nor::\n\n    > git clone git://github.com/ingydotnet/crockford-py.git\n    > cd crockford-py\n    > sudo make install\n\nUsage\n-----\n\n    import crockford\n\n    base32 = crockford.b32encode(string)\n    string = crockford.b32decode(base32)\n\nAuthors\n-------\n\n* Ingy dot Net <ingy@ingy.net>\n\nCopyright\n---------\n\ncrockford is Copyright (c) 2011, Ingy dot Net\n\ncrockford is licensed under the New BSD License. See the LICENSE file.\n',
  'name': 'crockford',
  'packages': ['crockford'],
  'scripts': [],
  'url': 'http://github.com/ingydotnet/crockford-py/',
  'version': '0.0.2'}
)
    return info
