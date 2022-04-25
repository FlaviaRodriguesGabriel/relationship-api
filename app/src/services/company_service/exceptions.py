__all__ = [
    "ClientIdMismatch",
]


from typing import final
from uuid import UUID

from requests.status_codes import codes

from exceptions import RelationshipApiException


@final  # won't allow inheritance from this class
class ClientIdMismatch(RelationshipApiException):
    # FIXME: this code is not being properly propagated to request return via Flask API
    status_code: int = codes.unprocessable_entity

    input_client_id: UUID
    queried_client_id: UUID

    def __init__(
        self,
        *args,
        input_client_id: UUID,
        queried_client_id: UUID,
        **kwargs,
    ) -> None:
        self.input_client_id = input_client_id
        self.queried_client_id = queried_client_id

        super().__init__(self.message, *args, **kwargs)

    @property
    def message(self):
        return (
            f"Input client id #{self.input_client_id} cannot be different"
            f" from the id obtained from external query: #{self.queried_client_id}"
        )
