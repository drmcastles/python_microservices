import grpc
from concurrent import futures
from grpc_reflection.v1alpha import reflection
import uuid
import user_service_pb2
import user_service_pb2_grpc


class UserServiceImplementation(user_service_pb2_grpc.UserServiceServicer):
    def __init__(self):
        self.users = {}

    def CreateUser(self, request, context):
        user_id = str(uuid.uuid4())
        self.users[user_id] = {"name": request.name, "email": request.email}
        return user_service_pb2.UserResponse(user_id=user_id, name=request.name, email=request.email)

    def GetUser(self, request, context):
        user = self.users.get(request.user_id)
        if user is None:
            return user_service_pb2.UserResponse()
        return user_service_pb2.UserResponse(user_id=request.user_id, name=user["name"], email=user["email"])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_service_pb2_grpc.add_UserServiceServicer_to_server(UserServiceImplementation(), server)

    # Включение Reflection API
    SERVICE_NAMES = (
        user_service_pb2.DESCRIPTOR.services_by_name['UserService'].full_name,
        reflection.SERVICE_NAME,  # Reflection service name
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port('[::]:5001')
    print("UserService server running on port 5001...")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()