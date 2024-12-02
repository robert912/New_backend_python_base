from flask_restful import Resource

class Prueba(Resource):
    def get(self):
        return {'message': 'La API está funcionando correctamente'}, 200

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b