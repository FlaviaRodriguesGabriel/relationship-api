#!/usr/bin/env bash

# Comment here
protoc -I=app/relationship-api/stubs/ --python_out=app/relationship-api/stubs/ --grpc_python_out=app/relationship-api/stubs/ app/relationship-api/stubs/relationship.proto

# Comment here
python -m grpc_tools.protoc -I=app/relationship-api/stubs/ --python_out=app/relationship-api/stubs/ --grpc_python_out=app/relationship-api/stubs/ app/relationship-api/stubs/relationship.proto

# Comment here
python -m grpc_tools.protoc -I ../protobufs --python_out=. \
         --grpc_python_out=. ../protobufs/recommendations.proto

# Comment here
# protoc -I=app/relationship-api/stubs/ --python_out=app/relationship-api/stubs/ app/relationship-api/stubs/relationship_service.proto
