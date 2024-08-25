from utils import memoize, get_json
from typing import Dict
class OrganizationClient:
    ORG_URL = "https://google.com/orgs/{org}"

    def __init__(self, org_name):
        self._org_name = org_name

    @memoize
    def org(self) -> Dict:
        """Memoize org"""
        return get_json(self.ORG_URL.format(org=self._org_name))


client = OrganizationClient("OpenAI")
org_data = client.org()
print(org_data)
