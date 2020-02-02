# funcfile
Turn a file into a Python function

Currently just a toy, but eg `python3 main.py` imports testfunc.py and makes testfunc available as a function that can be called.

Adding arguments would be fairly straightforward (add some ast.arg instances to the args list) and hacking Python's import machinery would be evil and cool.
