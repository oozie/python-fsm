#!/usr/bin/env python
print __file__
"""An implementation of the Finite State Machine.

This module can be used to build and describe finite-state automata.

The list of implemented FSM types:

 - FiniteStateMachine -- a semiautomaton base for all following classes.
   This class implements the process() method which takes an iterator
   as input and processes it.
   http://en.wikipedia.org/wiki/Semiautomaton

 - Acceptor -- an acceptor returning either True or False from the process()
   method depending on whether its final state is classified as accepting
   or not.
   http://en.wikipedia.org/wiki/Finite_state_machine#Acceptors_and_recognizers

 - Transducer -- a transducer class extends FiniteStateMachine by implementing
   an output() method which takes an input value passed to a the current
   state and returns current state's name.
   http://en.wikipedia.org/wiki/Finite-state_machine#Transducers

 - MooreMachine -- a specialized transducer. Its output() method returns
   an output value stored in the current state.
   http://en.wikipedia.org/wiki/Moore_machine

 - MealyMachine -- another specialized transducer. Its output() method returns 
   a value assigned to the transition that the input value caused.
   http://en.wikipedia.org/wiki/Mealy_machine
"""

import sys
import os
from distutils.core import setup

src_path = os.path.dirname(os.path.realpath(__file__)) + '/src'
sys.path.insert(0, src_path)
from fsm import __version__

setup(name='python-fsm',
      version=__version__,
      license='BSD',
      description='Finite State Machines',
      long_description=__doc__,
      author='Slawek Ligus',
      author_email='root@ooz.ie',
      url='https://github.com/oozie/python-fsm',
      download_url='http://python-fsm.googlecode.com/files/python-fsm-%s.tar.gz' % __version__,
      package_dir={'': 'src'},
      py_modules=['fsm'],
     )

