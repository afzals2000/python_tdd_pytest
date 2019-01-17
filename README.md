# Python TDD using Pytest
A Guideline how to write Test Driven Development in Python using Pytest

## Installation
Python 3.__x__ should be available on OS. Create virtual environment in $HOME dir ($HOME/venv3 __x__) 

## Usage Example
Setup
```
$:~/mypytest$ source ~/venv36/bin/activate;
$:~/mypytest$ pip install -r requirements.txt
```

Run all test verbose
```
$pytest -v
```

Run all test with tests print
```
$pytest -s
```

Run a specific tests
```
$pytest -q -s ./test/maths/test_my_math.py
```

## Change Log
* 0.0.1
   * Work in progress

## Meta
https://github.com/afzals2000/python_tdd_pytest

## Contributing
1. Fork it (https://github.com/afzals2000/python_tdd_pytest)
2. Create your feature branch (git checkout -b feature/fooBar)
3. Commit your changes (git commit -am 'Add some fooBar')
4. Push to the branch (git push origin feature/fooBar)
5. Create a new Pull Request