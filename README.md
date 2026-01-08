# Linear Math Mini Library

A library for working with linear algebra, vectors, matrices, etc. 

## Installing

Download the last version just from GitHub:

```bash
pip install git+https://github.com/boryspronin52-netizen/linear-math-mini-library.git
```

## Import
```python
import linear_math
```

## Vector class

### Propeties

```python
vector = Vector(1.0, 2.0, 3.0)

vector_normalized = vector.normalized           # returns normalized vector
vector_length = vector.length                   # returns the length of the vector
vector_xyz = vector.xyz                         # returns the end of the vector
```

### Operators

```python
vector_a = Vector(1.0, 1.0, 1.0)
vector_b = Vector(2.0, 3.0, 1.0)

vector_sum = vector_a + vector_b                # +
vector_dif = vector_a - vector_b                # -
vector_prod = vector_a * vector_b               # *
vector_quot = vector_a / vector_b               # /
```

### Functions

```python
vector_a = Vector(1.0, 1.0, 1.0)
vector_b = Vector(2.0, 3.0, 1.0)

dot_product = vector_a.dot(vector_b)            # dot product method

vector_a.normalize()                            # normalizes the vector 
```

## Matrix class

### Operators

```python
matrix_a = Matrix([[1.0, 2.0, 3.0],
                   [2.0, 1.0, 3.0],
                   [4.0, 2.0, 1.0]])

matrix_b = Matrix([[9.0, 8.0, 7.0],
                   [8.0, 5.0, 9.0],
                   [1.0, 8.0, 4.0]])

matrix_sum = matrix_a + matrix_b                # +
matrix_dif = matrix_a - matrix_b                # -

matrix_prod_with_matrix = matrix_a * matrix_b   # matrix * matrix
matrix_prod_with_number = matrix_a * 3.0        # matrix * number
```