## python map, filter and reduce

# map
`map(function_to_apply, list_of_inputs)`

e.g.
```
>>> list(map(lambda x:x+1, [1,2,3]))
>>> [2,3,4]
```

# filter
creates a list of elements for which a function returns true.
`filter(function_to_apply, list_of_inputs)`

e.g.
```
>>> list(filter(lambda x: x>1, [1,2,3]))
>>> [2,3]
```

# reduce
rolling compute sequential pairs of values in a list.
`reduce(function_to_apply, list_of_inputs)`

e.g.
```
>>> from functools import reduce
>>> reduce((lambda x,y: x+y), [1,2,3])
>>> 6
```

