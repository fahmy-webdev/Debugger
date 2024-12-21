import sys

class Debugger:
    def __init__(self, filename):
        self.filename = filename
        self.breakpoints = set()
        self.locals = {}
        self.watch_vars = set()

    def set_breakpoint(self, lineno):
        self.breakpoints.add(lineno)  

    def watch_variable(self, var_name):
        self.watch_vars.add(var_name) 

    def run(self): 
        sys.settrace(self.trace_calls)
        try:
            with open(self.filename) as f:
                code = f.read()
            exec(code, {}, self.locals)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            sys.settrace(None)

    def trace_calls(self, frame, event, arg):
        if event == 'call':
            return self.trace_lines
        return None

    def trace_lines(self, frame, event, arg):
        if event != 'line':
            return self.trace_lines

        lineno = frame.f_lineno
        if lineno in self.breakpoints:
            print(f"\n[DEBUG] Breakpoint hit at line {lineno}")
            self.print_debug_info(frame)
            input("Type anything and press Enter to continue...")
        return self.trace_lines

    def print_debug_info(self, frame):
        print("Local variables:")
        for var, val in frame.f_locals.items():
            print(f"  {var} = {val}")
        
        if self.watch_vars:
            print("\n[WATCH] Watched Variables:")
            for var in self.watch_vars:
                if var in frame.f_locals:
                    print(f"  {var} = {frame.f_locals[var]}")
                else:
                    print(f"  {var} is not defined")

if __name__ == "__main__":
    debugger = Debugger("test_script.py")
    debugger.set_breakpoint(6)
    debugger.set_breakpoint(9)  
    debugger.set_breakpoint(13)
    debugger.set_breakpoint(16) 
    debugger.watch_variable("message")   
    debugger.run()

