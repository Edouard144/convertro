LENGTH = {
    "mm": 0.001, "cm": 0.01, "m": 1, "km": 1000,
    "inch": 0.0254, "foot": 0.3048, "mile": 1609.344,
}

WEIGHT = {
    "mg": 0.000001, "g": 0.001, "kg": 1,
    "oz": 0.0283495, "lb": 0.453592,
}


def _convert(value, from_unit, to_unit, table):
    from_unit, to_unit = from_unit.lower(), to_unit.lower()
    if from_unit not in table or to_unit not in table:
        raise ValueError(f"Unknown unit. Choose from: {', '.join(table)}")
    return value * table[from_unit] / table[to_unit]


def length(value, from_unit, to_unit):
    return _convert(value, from_unit, to_unit, LENGTH)


def weight(value, from_unit, to_unit):
    return _convert(value, from_unit, to_unit, WEIGHT)


def temperature(value, from_unit, to_unit):
    f, t = from_unit.lower(), to_unit.lower()
    if f not in ("c", "f", "k") or t not in ("c", "f", "k"):
        raise ValueError("Temperature units: c, f, k")
    if f == "c":
        celsius = value
    elif f == "f":
        celsius = (value - 32) * 5 / 9
    else:
        celsius = value - 273.15
    if t == "c":
        return celsius
    if t == "f":
        return celsius * 9 / 5 + 32
    return celsius + 273.15