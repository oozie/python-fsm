# python-fsm
Python Finite State Machine implementation with a pygraphviz hook.
## TCP/IP state transitions
![TCP/IP](http://js-hosting.appspot.com/images/tcpip.png)
```
#!/usr/bin/python

from fsm import FiniteStateMachine, get_graph, State

STATES = ['LISTEN', 'SYN RCVD', 'ESTABLISHED', 'SYN SENT', 
          'FIN WAIT 1', 'FIN WAIT 2', 'TIME WAIT', 'CLOSING', 'CLOSE WAIT',
          'LAST ACK']

tcpip = FiniteStateMachine('TCP IP')

closed = State('CLOSED', initial=True)
listen, synrcvd, established, synsent, finwait1, finwait2, timewait, \
closing, closewait, lastack = [State(s) for s in STATES]

timewait['(wait)'] = closed
closed.update({r'passive\nopen': listen,
               'send SYN': synsent})

synsent.update({r'close /\ntimeout': closed,
                r'recv SYN,\nsend\nSYN+ACK': synrcvd,
                r'recv SYN+ACK,\nsend ACK': established})

listen.update({r'recv SYN,\nsend\nSYN+ACK': synrcvd,
               'send SYN': synsent})

synrcvd.update({'recv ACK': established,
                'send FIN': finwait1,
                'recv RST': listen})

established.update({'send FIN': finwait1,
                    r'recv FIN,\nsend ACK': closewait})

closewait['send FIN'] = lastack

lastack['recv ACK'] = closed

finwait1.update({'send ACK': closing,
                 'recv ACK': finwait2,
                 r'recv FIN, ACK\n send ACK': timewait})

finwait2[r'recv FIN,\nsend ACK'] = timewait

closing[r'recv\nACK'] = timewait

graph = get_graph(tcpip)
graph.draw('tcp.png', prog='dot')
```

## Dublin City Council Parking Meter (2011)
![Irish Park-o-meter](http://js-hosting.appspot.com/images/parking.png) 
```
"""A Moore Machine modeled on Dublin's City parking meters."""
from fsm import *

parking_meter = MooreMachine('Parking Meter')

ready = State('Ready', initial=True)
verify = State('Verify')
await_action = State(r'Await\naction')
print_tkt = State('Print ticket')
return_money = State(r'Return\nmoney')
reject = State('Reject coin')
ready[r'coin inserted'] = verify

verify.update({'valid': State(r'add value\rto ticket'), 
               'invalid': reject})

for coin_value in verify:
    verify[coin_value][''] = await_action

await_action.update({'print': print_tkt,
                     'coin': verify,
                     'abort': return_money,
                     'timeout': return_money})
return_money[''] = print_tkt[''] = ready
get_graph(parking_meter).draw('parking.png', prog='dot')
```
## Binary Adder
![Binary Adder](http://js-hosting.appspot.com/images/adder.png)
```
adder = MealyMachine('Binary addition')

carry = State('carry')
nocarry = State('no carry', initial=True)

nocarry[(1, 0), 1] = nocarry
nocarry[(0, 1), 1] = nocarry
nocarry[(0, 0), 0] = nocarry
nocarry[(1, 1), 0] = carry

carry[(1, 1), 1] = carry
carry[(0, 1), 0] = carry
carry[(1, 0), 0] = carry
carry[(0, 0), 1] = nocarry

number1 = list(int (i) for i in '0001010')
number2 = list(int (i) for i in '0001111')

inputs = zip(number1, number2)

print list(adder.process(inputs[::-1]))[::-1]
```
the code above will print [0, 0, 1, 1, 0, 0, 1] 
