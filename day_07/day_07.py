#!/usr/bin/env python3

# Automatic submission does not appear to be working.
import aocd
import re


class Program:
    def __init__(self, data):
        match = re.search("\s*(?P<name>[a-z]+)\s+\((?P<weight>\d+)\)\s*(->)?\s*(?P<children>.*)\s*", data)
        self.name = match.group('name')
        self.weight = int(match.group('weight'))
        self._children = [] if len(match.group('children')) == 0 else match.group('children').split(', ')
        self.parent = None

    def __len__(self):
        return len(self._children)

    def __getitem__(self, item):
        return self._children[item]

    def __repr__(self):
        rep = "{} ({})".format(self.name, self.weight)
        if len(self._children) > 0:
            rep = rep + ' -> ' + ', '.join(self._children)
        return rep

    def __str__(self):
        return self.name


def parse_programs(data):
    """
    Parse the programs into a table; they are also represeented as a tree.
    :param data:
    :return: the table of programs
    """
    progs = [Program(line) for line in data.split('\n')]
    program_tree = {p.name: p for p in progs}

    for p in progs:
        for c in p:
            program_tree[c].parent = p

    # Find the program with no parent.
    return program_tree


def find_head_program(programs):
    """
    Find the program at the head of the tree.
    :param programs: the table of programs
    :return: the program that has no parent

    >>> programs = []
    >>> programs.append('pbga (66)')
    >>> programs.append('xhth (57)')
    >>> programs.append('ebii (61)')
    >>> programs.append('havc (66)')
    >>> programs.append('ktlj (57)')
    >>> programs.append('fwft (72) -> ktlj, cntj, xhth')
    >>> programs.append('qoyq (66)')
    >>> programs.append('padx (45) -> pbga, havc, qoyq')
    >>> programs.append('tknk (41) -> ugml, padx, fwft')
    >>> programs.append('jptl (61)')
    >>> programs.append('ugml (68) -> gyxo, ebii, jptl')
    >>> programs.append('gyxo (61)')
    >>> programs.append('cntj (57)')
    >>> find_head_program(parse_programs('\\n'.join(programs))).name
    'tknk'
    """
    return next(filter(lambda prog: prog.parent is None, programs.values()))


def find_unbalanced_program(programs):
    head = find_head_program(programs)


if __name__ == '__main__':
    session = aocd.get_cookie()
    data = aocd.get_data(day=7, year=2017, session=session)
    programs = parse_programs(data)

    a1 = find_head_program(programs)
    print("a1 = %r" % a1)
    a2 = None
    aocd.submit1(a1, day=1, year=2017, session=session, reopen=False)
    print("a2 = %r" % a2)
    aocd.submit2(a1, day=1, year=2017, session=session, reopen=False)
