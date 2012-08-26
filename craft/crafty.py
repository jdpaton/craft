import os
import sys
import argparse
import inspect

from termcolor import cprint, colored

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
        print("Running task: [ {} ]".format(tprint))
        task.all[t]()
      else:
        err = colored("ERR", 'red')
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

task = TaskRegistrar()



