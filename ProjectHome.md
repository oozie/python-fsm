# Finite State Machines in Python #
python-fsm module can be used to build and describe deterministic finite-state automata.

## Example: Operation of a microwave oven ([full list of examples](http://code.google.com/p/python-fsm/w/list?q=label:Examples)) ##


<img src='http://js-hosting.appspot.com/images/microwave.png' width='100%' />
```
from fsm import State, Transducer, get_graph

microwave = Transducer('Microwave Oven')

closed_i = State(r'CLOSED\nidle', initial=True)
closed_p = State(r'CLOSED\nprocessing')
opened_i = State(r'OPEN\nidle')
paused = State('PAUSED')
settings = State(r'SETUP')

closed_i[r'PSB, TK /\nset program,\nset timer'] = closed_i
closed_i['SSB / start'] = closed_p
closed_i['ODH / open door'] = opened_i
closed_i['ELS / enter setup'] = settings
settings['SSB / save setup'] = settings
settings['ELS / leave setup'] = closed_i
opened_i['DL / shut door'] = closed_i
closed_p['PRB / pause'] = paused
closed_p['ODH / open door'] = opened_i
closed_p['TO / ready'] = closed_i
paused['SSB / stop'] = closed_i
paused['PRB / resume'] = closed_p
paused[r'PSB, TK /\nreset program,\nreset timer'] = paused
paused['ODH / open door'] = opened_i

get_graph(microwave).draw('microwave.png', prog='dot')
```

## Overview of implemented types ##

At the center of the module is the **State** class representing a state which can be used in a finite state machine of any type. States can be used in the following automata:

### FiniteStateMachine ###
Semiautomaton base for all types that follow. This class implements the process() method which takes an iterator as input and processes it. Semiautomata don't return any values from process()
http://en.wikipedia.org/wiki/Semiautomaton

### Acceptor ###
Acceptor's process() will return either True or False depending on whether its final state is classified as accepting or not.
http://en.wikipedia.org/wiki/Finite_state_machine#Acceptors_and_recognizers

### Transducer ###
Transducer class extends FiniteStateMachine by implementing an output() method which takes an input value which is meant to be passed to a the current state and returns current state's name.
http://en.wikipedia.org/wiki/Finite-state_machine#Transducers

### MooreMachine ###
A specialized transducer. Its output() method returns an output value stored in the current state.
http://en.wikipedia.org/wiki/Moore_machine

### MealyMachine ###
another specialized transducer. Its output() method returns a value assigned to the transition that the input value caused.