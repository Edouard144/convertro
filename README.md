# convertro

A simple unit converter for length, weight and temperature.

## Install

```
pip install convertro
```

## Usage

```python
from convertro import length, weight, temperature

length(5, "km", "mile")        # 3.106...
weight(2, "kg", "lb")          # 4.409...
temperature(100, "c", "f")     # 212.0
```

## Units

- **Length:** mm, cm, m, km, inch, foot, mile
- **Weight:** mg, g, kg, oz, lb
- **Temperature:** c, f, k