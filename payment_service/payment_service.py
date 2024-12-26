import grpc
from concurrent import futures
from grpc_reflection.v1alpha import reflection
import uuid

import payment_service_pb2
import payment_service_pb2_grpc


class PaymentServiceImplementation(payment_service_pb2_grpc.PaymentServiceServicer):
    def __init__(self):
        self.payments = {}

    def CreatePayment(self, request, context):
        payment_id = str(uuid.uuid4())
        self.payments[payment_id] = {"order_id": request.order_id, "amount": request.amount, "status": "Processed"}
        return payment_service_pb2.PaymentResponse(payment_id=payment_id, order_id=request.order_id, amount=request.amount, status="Processed")

    def GetPayment(self, request, context):
        payment = self.payments.get(request.payment_id)
        if payment is None:
            return payment_service_pb2.PaymentResponse()
        return payment_service_pb2.PaymentResponse(payment_id=request.payment_id, order_id=payment["order_id"], amount=payment["amount"], status=payment["status"])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    payment_service_pb2_grpc.add_PaymentServiceServicer_to_server(PaymentServiceImplementation(), server)

    # Включение Reflection API
    SERVICE_NAMES = (
        payment_service_pb2.DESCRIPTOR.services_by_name['PaymentService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port('[::]:5003')
    print("PaymentService server running on port 5003...")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()