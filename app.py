from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import random
import math 

app = Flask(__name__)
api = Api(app)

# Create a basic resource that simulate backend service
class ServiceA(Resource):
    def get(self):
        return jsonify({'message': 'Hello from Service A!'})

class LoadBalanceService(Resource):
    def get(self):
        services = [
            {'name': 'Service A Instance 1', 'msg': 'Service A is up and running'},
            {'name': 'Service A Instance 2', 'msg': 'Service A is up and running'},
        ]
        service = random.choice(services)
        return jsonify({'message': service['msg']})

class ServiceB(Resource):
    def get(self):
        return jsonify({'message': 'Hello from Service B!'})
    
class LoadBalanceServiceB(Resource):
    def get(self):
        services = [
            {'name': 'Service B Instance 1', 'msg': 'Service B is up and running'},
            {'name': 'Service B Instance 2', 'msg': 'Service B is up and running'},
        ]
        service = random.choice(services)
        return jsonify({'message': service['msg']})
        
class ServiceC(Resource):
    def get(self):
        return jsonify({'message': 'Hello from Service C!'})

class LoadBalanceServiceC(Resource):
    def get(self):
        services = [
            {'name': 'Service C Instance 1', 'msg': 'Service C is up and running'},
            {'name': 'Service C Instance 2', 'msg': 'Service C is up and running'},
        ]
        service = random.choice(services)
        return jsonify({'message': service['msg']})
    
class SendNotifications(Resource):
    def get(self):
      notifications = [
          {'id': 1, 'title': 'New Order', 'content': 'An order has been placed.'},
          {'id': 2, 'title': 'Payment Received', 'content': 'Your payment has been received.'},
          {'id': 3, 'title': 'Order Shipped', 'content': 'Your order has been shipped.'},
          {'id': 4, 'title': 'Order Delivered', 'content': 'Your order has been delivered.'},
          {'id': 5, 'title': 'Invoice Generated', 'content': 'Your invoice has been generated.'},
      ]
      
      return jsonify({'notifications': notifications})

class JoinServices(ServiceA):
    def get(self):
        return jsonify({'message': 'Hello from Service A and Service B!'})

class JoinServicesAandC(ServiceA, ServiceC):
    def get(self):
        return jsonify({'message': 'Hello from Service A and Service C!'})

class JoinServicesBandC(ServiceB, ServiceC):
    def get(self):
        return jsonify({'message': 'Hello from Service B and Service C!'})

class ReportErrorService(Resource):
    def get(self):
        failed_services = [
            {'name': 'Service A','error': 'Failed to connect to database.'},
            {'name': 'Service B','error': 'Failed to connect to database.'},
            {'name': 'Service C','error': 'Failed to connect to database.'},
        ]
        return jsonify({'failed_services': failed_services})

class CalculateExpensesService(Resource):
    def get(self):
        expenses = [
            {'id': 1, 'description': 'Rent', 'amount': 500},
            {'id': 2, 'description': 'Milk', 'amount': 20},
            {'id': 3, 'description': 'Groceries', 'amount': 100},
            {'id': 4, 'description': 'Petrol', 'amount': 30},
            {'id': 5, 'description': 'Car Maintenance', 'amount': 150},
        ]
        return jsonify({'expenses': expenses})
    
# Register the resources with the API

api.add_resource(ServiceA, '/serviceA')
api.add_resource(ServiceB, '/serviceB')
api.add_resource(ServiceC, '/serviceC')
api.add_resource(LoadBalanceService, '/loadBalanceA')

api.add_resource(LoadBalanceServiceB, '/loadBalanceB')

api.add_resource(LoadBalanceServiceC, '/loadBalanceC')

api.add_resource(SendNotifications, '/notifications')

api.add_resource(JoinServices, '/joinServicesAandB')

api.add_resource(JoinServicesAandC, '/joinServicesAandC')

api.add_resource(JoinServicesBandC, '/joinServicesBandC')

api.add_resource(ReportErrorService, '/reportError')

api.add_resource(CalculateExpensesService, '/calculateExpenses')

        
# Run the flask application
if __name__ == '__main__':
    app.run(debug=True)