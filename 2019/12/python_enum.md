
## python enum

Enumeration class
```
from enum import Enum
class A(Enum):
    a = 1
    b = 2
```

Get enumerate items:
```
for i,j in A.__members__.items():
    i,j
```

Attention:
`A.a.value` isn't equals to `A.a`
