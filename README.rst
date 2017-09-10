TfL API - Transport for London - Python Client
=========================================

This is a beta client for the `Transport for London <https://tfl.gov.uk/>`__
Beta Api.

Compatible with Python 2 and 3. No dependencies required.

More documentation to come, but a simple usage:

.. code:: python

    from tfl_api import TfLAPI
    api = TfLAPI({app_id="1234567", app_key="11bbccdd"})
    response = api.get_line_arrivals("c2", "490003380N")
    print (response.code)
    ### 200
    print (response.data)
    ### { JSON }
