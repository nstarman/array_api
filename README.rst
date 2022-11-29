Array API Implementation for All
################################

Example:

>>> import array_api as ap
>>> import numpy.array_api as np

>>> x = np.linspace(1, 2, num=5)[:, None]
>>> x
Array([[1.  ],
       [1.25],
       [1.5 ],
       [1.75],
       [2.  ]], dtype=float64)

>>> np.cos(x)  # specific library
Array([[ 0.54030231],
       [ 0.31532236],
       [ 0.0707372 ],
       [-0.17824606],
       [-0.41614684]], dtype=float64)


>>> ap.cos(x)  # universal library
Array([[ 0.54030231],
       [ 0.31532236],
       [ 0.0707372 ],
       [-0.17824606],
       [-0.41614684]], dtype=float64)
