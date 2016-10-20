- ``sudo pip install json-delta``  # **install** ``json-delta``

```
Collecting json-delta
/usr/local/lib/python2.7/site-packages/pip/_vendor/requests/packages/urllib3/util/ssl_.py:318: SNIMissingWarning: An HTTPS request has been made, but the SNI (Subject Name Indication) extension to TLS is not available on this platform. This may cause the server to present an incorrect TLS certificate, which can cause validation failures. You can upgrade to a newer version of Python to solve this. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#snimissingwarning.
  SNIMissingWarning
  Downloading json_delta-2.0-py2.py3-none-any.whl
Installing collected packages: json-delta
```

----

- http://json-delta.readthedocs.io/en/latest/json_diff.1.html

```sh
json_diff -u FILE_1.json FILE_2.json  |  less
