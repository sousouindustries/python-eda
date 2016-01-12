Event-Driven Architecture Framework
===================================


Synopsis
--------
The Python ``eda`` module provides a framework to create Python applications
in Event-Driven Architectures (EDAs).


Features
--------
The module provides the following major features:

-   A syntax to declaratively specify event types and their structure.
-   Local implementations of an enterprise message bus, using threads
    (for single-process architectures) or processes.
-   An interface specification of the enterprise message bus; allowing
    additional, more mature implementations (using for example, Apache
    Apollo).
-   A framework to quickly prototype and deploy services.


Installation
------------
To install ``eda``, run the following command in your terminal:

.. code-block:: bash

    $ pip install eda

Alternatively, you may clone the GitHub repository to install the latest
development branch. This method provides the following options:

1.  Run ``python3 setup.py install``.
2.  Run ``make links``. This will create symbolic links in the systems' Python library
    directory. Provided as a conveniance when developing the module in cooperation with
    other packages or applications.

