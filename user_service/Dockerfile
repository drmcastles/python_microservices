# Базовый образ
FROM python:3.10-slim

# Установка зависимостей
RUN pip install --no-cache-dir grpcio grpcio-tools
RUN pip install grpcio grpcio-tools grpcio-reflection

# Копируем код
WORKDIR /app
COPY . .

# Генерация gRPC файлов
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. user_service.proto

EXPOSE 5001

# Запуск сервиса
CMD ["python", "user_service.py"]
