<img src='http://js-hosting.appspot.com/images/tcpip.png' width='100%' />
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