from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema

greeting_schema = {
    "type": "object",
    "properties": {
        "greetee": {
            "type": "string",
        }
    },
    "required": ["greetee"],
}


class GreetingInputs(Inputs):
    json = [JsonSchema(schema=greeting_schema)]


def validate_partnership(request):
    inputs = GreetingInputs(request)
    if inputs.validate():
        return None
    else:
        return inputs.errors
