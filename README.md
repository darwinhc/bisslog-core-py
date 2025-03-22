# bisslog-core-py

It is an auxiliary library for the business layer or service domain, which allows to have a common language for operations when interacting with external components that are part of the infrastructure of the same. In other words, the business rules will not change if the architect decided to change the messaging system, it does not matter. The essential point of this library is that the domain should not change because some adapter changed.






## Tests

To Run test with coverage
~~~cmd
coverage run --source=bisslog_core -m pytest tests/
~~~


To generate report
~~~cmd
coverage html && open htmlcov/index.html
~~~