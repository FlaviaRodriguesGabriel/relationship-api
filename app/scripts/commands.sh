#!/usr/bin/env bash

# Generate files to use after changing '*.proto' files:
python -m grpc_tools.protoc -I=src/stubs/ --python_out=src/stubs/ --grpc_python_out=src/stubs/ src/stubs/relationship.proto

# Comment here
# protoc -I=app/relationship-api/stubs/ --python_out=app/relationship-api/stubs/ --grpc_python_out=app/relationship-api/stubs/ app/relationship-api/stubs/relationship.proto

# python -m grpc_tools.protoc -I=app/relationship-api/stubs/ --python_out=app/relationship-api/stubs/ --grpc_python_out=app/relationship-api/stubs/ app/relationship-api/stubs/relationship.proto

# python -m grpc_tools.protoc -I ../protobufs --python_out=. \
#          --grpc_python_out=. ../protobufs/recommendations.proto

# protoc -I=app/relationship-api/stubs/ --python_out=app/relationship-api/stubs/ app/relationship-api/stubs/relationship_service.proto
