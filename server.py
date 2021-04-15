import grpc
import time

from concurrent import futures

import calculator_pb2
import calculator_pb2_grpc

import math_util


class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def SquareRoot(self, request, context):
        response = calculator_pb2.Number()
        response.value = math_util.square_root(request.value)
        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# adding class to server
calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)

print('starting server....')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    server.stoop(0)
