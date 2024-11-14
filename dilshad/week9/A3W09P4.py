class Converter:
    def __init__(self, input_value, unit) -> None:
        self.input_value = input_value
        self.unit = unit
        # Convert the input value to meters (base unit)
        self.value_in_meters = self.convert_to_meters()

    def convert_to_meters(self):
        if self.unit == "inches":
            return self.input_value * 0.0254
        elif self.unit == "feet":
            return self.input_value * 0.3048
        elif self.unit == "yards":
            return self.input_value * 0.9144
        elif self.unit == "miles":
            return self.input_value * 1609.34
        elif self.unit == "kilometers":
            return self.input_value * 1000
        elif self.unit == "centimeters":
            return self.input_value * 0.01
        elif self.unit == "millimeters":
            return self.input_value * 0.001
        else:
            return self.input_value

    def inches(self):
        return self.value_in_meters / 0.0254

    def feet(self):
        return self.value_in_meters / 0.3048

    def yards(self):
        return self.value_in_meters / 0.9144

    def miles(self):
        return self.value_in_meters / 1609.34

    def kilometers(self):
        return self.value_in_meters / 1000

    def meters(self):
        return self.value_in_meters

    def centimeters(self):
        return self.value_in_meters / 0.01

    def millimeters(self):
        return self.value_in_meters / 0.001

    def __str__(self):
        return f"<{self.__class__.__name__} object at {hex(id(self))}>"
