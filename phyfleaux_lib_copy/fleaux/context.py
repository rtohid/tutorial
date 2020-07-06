from __future__ import annotations

__license__ = """
Copyright (c) 2020 R. Tohid

Distributed under the Boost Software License, Version 1.0. (See accompanying
file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
"""

__doc__ = """
# In computer engineering, computer architecture is a set of rules and methods
# that describe the functionality, organization, and implementation of computer
# systems. 
A set of rules and methods describing functionality, organization, and implementation of computer systems. 
"""
import ast

from collections import defaultdict
from inspect import getsource
from typing import Callable


class Task(ast.NodeVisitor):
    class _Python:
        pass

    def __init__(self, fn: [Task, Callable]) -> None:
        """
        Phyfleaux callable.

        :arg fn: Python callable, either a python function or another
            :class:`task`.
        :arg executor: target executor (PhySL, Python, Numba, ...) each executor
            can be generated for multiple architecture (SIMT (GPU, mainly CUDA), MIMD(), SIMD).
        :arg cost_function: a callback function to quantify execution cost.
        """

        if isinstance(fn, Task):
            self = fn
            self.context.append(context)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
            self.cost.append(cost_function)

        # fn is a python function
        else:
            self.fn = fn
            self.context = [context]
            self.cost = [cost_function]

            # Python AST
            self.py_ast = ast.parse((getsource(fn)))
            self.id = hash(self.py_ast)

            self.physl = self.visit(self.py_ast.body[0])

        # self.input = defaultdict()
        self.input = list()
        for arg in self.py_ast.body[0].args.args:
            self.input.append(arg.arg)
            # self.input[arg.arg] = arg

    @property
    def context(self):
        pass

    def __call__(self, *args, **kwargs):
        return self.fn(*args, **kwargs)


"""
        self.ir = defaultdict(lambda: defaultdict())
        
        # maps hashes of nodes in :function:`fn`'s Python AST to their copy.
        for node in ast.walk(self.tree):
            self.ir[hash(node)] = deepcopy(node)
            setattr(self.ir[hash(node)], 'tiramisu', None)
"""