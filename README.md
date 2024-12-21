Python Debugger Project
Introduction
This project implements a custom Python debugger that allows users to:

Set breakpoints in a Python script.
Monitor variables during execution.
Features
Line-by-line debugging.
Variable watching for runtime analysis.
Integration with Pylint for code quality and Pytest for testing.
How to Use
Add your script to debug (e.g., test_script.py).
Use Debugger to set breakpoints and watch variables. Example:
from debugger import Debugger

debugger = Debugger("test_script.py")
debugger.set_breakpoint(10)
debugger.watch_variable("total")
debugger.run()
