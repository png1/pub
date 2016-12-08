## Preamble

To detect **'string'** types, but without using the ``six`` library:

- http://stackoverflow.com/questions/1549801/differences-between-isinstance-and-type-in-python
- http://stackoverflow.com/questions/4987327/how-do-i-check-if-a-string-is-unicode-or-ascii

```python
import types

def isString(s):  return isinstance(s, types.StringTypes)
```

Using the ``six`` library:

```python
import six

def isString(s):  return isinstance(s, six.string_types)
```

----

## Install

- ``sudo pip install six``  # **install** ``six``

```
Collecting six
  Downloading six-1.10.0-py2.py3-none-any.whl
Installing collected packages: six
Successfully installed six-1.10.0
```

----

## Docs

- https://pypi.python.org/pypi/six

- https://pythonhosted.org/six


#### Examples

- ``six.string_types``

- ``six.iteritems(...)``
