import os
import sys
import argparse
import inspect

from termcolor import cprint, colored


print_err = colored("ERR", 'red')
print_warn = colored("WARN", 'yellow')
print_ok = colored("OK", 'green')

def run():
  """Entry point"""
  task_list = ("\n".join(['- ' + t + ': ' + (inspect.getdoc(task.all[t]) or "") for t in task.all]))
  parser = argparse.ArgumentParser(epilog="Available tasks:\n\n{}".format(task_list), formatter_class=argparse.RawDescriptionHelpFormatter)
  parser.add_argument('task', nargs='*')
  args = parser.parse_args()

  if args.task:
    for t in args.task:
      tprint = colored(t, 'blue')
      if t in task.all:
        print("Running task: -> [ {} ]".format(tprint))
        if t in dependsRegister:
          for d in dependsRegister[t][1]:
            if d in task.all:
              print("Running task dependency: -> [ {} ]\n".format(colored(d, 'blue')))
              task.all[d]()
              print("."*5 + print_ok)
            else:
              print(print_warn + " Task [ {} ] not found, skipping".format(colored(d, 'blue')))

        task.all[t]()
        print("\n" + print_ok + " task \"{}\" successfully completed".format(t))

      else:
        print("{} Could not find task [ {} ] in the craftfile.".format(err, tprint))

def execfile():
  """Execute a crafty.py file using exec(). Requires no user imports"""
  filename = os.path.join(os.getcwd(), 'crafty.py')
  exec(compile(open(filename).read(), filename, 'exec'), globals(), locals())


def TaskRegistrar():
    """Keeps a dict of all tasks in the craftfile"""
    registry = {}
    def registrar(func):
        registry[func.__name__] = func
        return func  

    registrar.all = registry
    return registrar

dependsRegister = {}

def dependsRegistrar(*dargs, **dkwargs):
    """ dependency register in global dict.
       If called as a function directly, we don't get
       the function name, just the decorator arguments.
    """
    def wrap(f):
        dependsRegister[f.__name__] = [f, dargs]
        return f
    return wrap

task = TaskRegistrar()
depends = dependsRegistrar



