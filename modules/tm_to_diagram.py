from graphviz import Digraph
import re
def tm_to_diagram(tmString):
    tmString = tmString.replace('Eps', 'ε').replace('_', '␣')
    edges = []
    blocks = []
    for line in tmString.split('\n'):
        if 'block: ' in line:
            blocks.append(line)
        elif len(line) > 0:
            edges.append(line)

    g = Digraph()
    g.attr('node', shape='box')
    for line in blocks:
        [_, block, _] = re.split('block: |=', line)
        g.node(block)

    g.attr('node', shape='doublecircle')
    for line in edges:
        [src, dst, label] = re.split('->|: ', line)
        if dst in ['qA', 'qR', 'qH']:
            g.node(dst)

    g.attr('node', shape='circle')
    for line in edges:
        [src, dst, label] = re.split('->|: ', line)
        g.edge(src, dst, label=label)

    return g