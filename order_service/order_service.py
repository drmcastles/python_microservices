import grpc
from concurrent import futures
from grpc_reflection.v1alpha import reflection
import uuid

import order_service_pb2
import order_service_pb2_grpc


class OrderServiceImplementation(order_service_pb2_grpc.OrderServiceServicer):
    def __init__(self):
        self.orders = {}

    def CreateOrder(self, request, context):
        order_id = str(uuid.uuid4())
        self.orders[order_id] = {"user_id": request.user_id, "product_ids": list(request.product_ids)}
        print(f"Order created: {self.orders[order_id]}")
        return order_service_pb2.OrderResponse(order_id=order_id, user_id=request.user_id, product_ids=request.product_ids)

    def GetOrder(self, request, context):
        order = self.orders.get(request.order_id)
        if not order:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Order with ID {request.order_id} not found.")
            return order_service_pb2.OrderResponse()
        return order_service_pb2.OrderResponse(order_id=request.order_id, user_id=order["user_id"], product_ids=order["product_ids"])


def serve():
    try:
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        order_service_pb2_grpc.add_OrderServiceServicer_to_server(OrderServiceImplementation(), server)

        # Включение Reflection API
        SERVICE_NAMES = (
            order_service_pb2.DESCRIPTOR.services_by_name['OrderService'].full_name,
            reflection.SERVICE_NAME,
        )
        reflection.enable_server_reflection(SERVICE_NAMES, server)

        server.add_insecure_port('[::]:5002')
        print("OrderService server running on port 5002...")
        server.start()
        server.wait_for_termination()
    except Exception as e:
        print(f"Error starting OrderService: {e}")


if __name__ == '__main__':
    serve()
