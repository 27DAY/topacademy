
# TODO: 3 с/р

class Auto:

    def __init__(self, bodywork, motor, color):
        self._bodywork = bodywork
        self._motor = motor
        self._color = color

    def getInfo(self):
        return {
            'Кузов': self._bodywork,
            'Мотор': self._motor,
            'Цвет': self._color}