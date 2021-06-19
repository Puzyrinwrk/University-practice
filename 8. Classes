# Write a class that represents a matrix.

# Class should support following operations (see brief description with examples here, full theory (optional) can be found here ):

# multiplication on other matrix
# multiplication on scalar
# addition
# subtraction
# transposition
# constructor, 3 parameters:
# 1) number of rows
# 2) number of columns
# 3) generator function , produced values are 3-element tuple (row, column, value); order of appearance: a) tuples with lower rows numbers come first b) if rows are equal tuples with lower columns numbers come first; if value not produced for some cell, its default value is 0
# if order of appearance in generator function not satisfied throw an exception
# __repr__    (useful for debugging, method description)
# Implementation requirements:

# matrix data should be stored in 2-dimension tuple (tuple of tuples) to provide immutability, see: https://en.wikipedia.org/wiki/Immutable_object
# matrix data variable should have name data
# temporary objects of matrix size (rows * columns) are not allowed nor in constructor nor in operations code, maximum size of temporary object is max(rows, columns)
# each operation produces new matrix
# for most operations double loop (for i in ...: for j in ...) required, to make code more concise and clean use generic function for  looping and pass lambda function (that represents unique part of each operation) as parameter to it; at least following operations should use generic function: "multiplication on scalar", "subtraction", "addition", however optionally you may create advanced version that can be applied to "multiplication on other matrix" and "transposition" also

# Implementation hints:

# as temporary objects not allowed one of approaches to construct object is to use nested tuple generator
# simple example:
# >>> tuple(tuple (i*j for i in range(1,10)) for j in range(1,10))
# ((1, 2, 3, 4, 5, 6, 7, 8, 9),
# (2, 4, 6, 8, 10, 12, 14, 16, 18),
# (3, 6, 9, 12, 15, 18, 21, 24, 27),
# (4, 8, 12, 16, 20, 24, 28, 32, 36),
# (5, 10, 15, 20, 25, 30, 35, 40, 45),
# (6, 12, 18, 24, 30, 36, 42, 48, 54),
# (7, 14, 21, 28, 35, 42, 49, 56, 63),
# (8, 16, 24, 32, 40, 48, 56, 64, 72),
# (9, 18, 27, 36, 45, 54, 63, 72, 81))
# use gen_stream method from chapter 9 to fill cell with zero if value not returned by generator for some cell
# Class signature:

# class Matrix:
#    def __init__(self, rows, columns, gen)
#    def mult(self, other)
#    def mult_scalar(self, scalar)
#    def sum(self, other)
#    def subt(self, other)
#    def transpose(self)
#    def __repr__(self)
# If some operation can't be done (due to incompatible matrix sizes) ValueError exception (see https://docs.python.org/3/library/exceptions.html#ValueError) should be thrown.

# Example:
# def gen():
#    yield (0,0,1)
#    yield (0,1,2)
#    yield (1,0,1)
#    yield (1,2,1)
# m = Matrix(2,3,gen)
# print(m)
# (1, 2, 0)
# (1, 0, 1)
# m = m.mult(m.transpose())
# print(m)
# (5, 1)
# (1, 2)

from ch6_functions import gen_stream


class Matrix:
    def __init__(self, rows, columns, gen):
        self.rows = rows
        self.columns = columns
        generate = gen_stream(rows * columns, gen() if callable(gen) else gen, lambda x: (x[0] * columns + x[1], x[2]))
        self.data = tuple(tuple(next(generate) for _ in range(columns)) for _ in range(rows))

    def _oper(self, op):
        return Matrix(self.rows, self.columns,
                      (((i, j, op(i, j)) for i in range(self.rows) for j in range(self.columns))))

    def __call__(self, i, j):
        return self.data[i][j]

    def sum(self, other):
        if type(other) != Matrix:
            raise TypeError('Invalid type of Matrix')
        if other.rows != self.rows or other.columns != self.columns:
            raise ValueError('Invalid dimension of matrix')
        return self._oper(lambda x, y: self(x, y) + other(x, y))

    def subt(self, other):
        if type(other) != Matrix:
            raise TypeError('Invalid type of Matrix')
        if other.rows != self.rows or other.columns != self.columns:
            raise ValueError('Invalid dimension of matrix')
        return self._oper(lambda x, y: self(x, y) - other(x, y))

    def mult_scalar(self, scalar):
        if type(scalar) != int:
            raise ValueError('Invalid type')

        return self._oper(lambda x, y: self(x, y) * scalar)

    def mult(self, other):
        if self.columns != other.rows:
            raise ValueError('Invalid dimension of matrix')

        return Matrix(self.rows, other.columns, ((i, j, sum(self(i, k) * other(k, j) for k in range(self.columns)))
                                                 for i in range(self.rows) for j in range(other.columns)))

    def transpose(self):
        return Matrix(self.columns, self.rows, ((j, i, self.data[i][j])
                                                for j in range(self.columns) for i in range(self.rows)))

    def __repr__(self):
        return "\n".join(str(row) for row in self.data)


def gen():
    yield 0, 0, 1
    yield 0, 1, 2
    yield 1, 0, 1
    yield 1, 2, 1


m = Matrix(2, 3, gen)
print(m)
m = m.mult(m.transpose())
print(m)

