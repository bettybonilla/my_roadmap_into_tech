import csv
import json
from dataclasses import dataclass, is_dataclass, asdict


@dataclass
class Contact:
    name: str
    email: str


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if is_dataclass(o):
            return asdict(o)
        return super().default(o)


class EmailOrganizer(object):
    contacts_by_domain = {}

    @staticmethod
    def sanitize_data(data: str) -> str:
        data = data.strip().replace(u'\ufeff', '')
        return data

    @staticmethod
    def _parse_company_domain(email_addr: str) -> str:
        domain = email_addr.split('@')[1]
        return domain

    def bucket_contacts(self, email_addr: str, contact_name: str):
        domain = self._parse_company_domain(email_addr)
        contacts = self.contacts_by_domain.get(domain, None)
        # if the company is missing create a new contact list
        if contacts is None:
            contacts = [Contact(contact_name, email_addr)]
            self.contacts_by_domain[domain] = contacts
            return
        # the contact list exist so just return it
        if Contact(contact_name, email_addr) in contacts:
            return

        contacts.append(Contact(contact_name, email_addr))
        self.contacts_by_domain[domain] = contacts
        return

    def contacts_to_json(self) -> str:
        return json.dumps(self.contacts_by_domain, indent=4, sort_keys=True, cls=EnhancedJSONEncoder)


if __name__ in '__main__':
    eo = EmailOrganizer()

    print(type(eo))
