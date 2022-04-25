__all__ = [
    "PowerOIG",
]

from uuid import UUID, uuid5

from models import internal
from models.validators import CpfCnpj
from utils import Singleton


class PowerOIG(Singleton):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def _get_person_id(self, document_number: CpfCnpj) -> UUID:
        # TODO: implement REST api call to 'Power OIG' service in order to obtain the unique identifier of this person
        return uuid5(
            namespace=UUID("{12345678-1234-5678-1234-567812345678}"),
            name=document_number,
        )

    def get_company_id(self, company: internal.Client) -> UUID:
        return self._get_person_id(company.origination_document.number)

    def get_partner_id(self, partner: internal.Client) -> UUID:
        return self._get_person_id(partner.origination_document.number)
