class Company:
    def __init__(self, company_name, location, company_id=None):
        self._company_id = company_id
        self._company_name = company_name
        self._location = location

    @property
    def company_id(self):
        return self._company_id

    @company_id.setter
    def company_id(self, value):
        if value is not None and not isinstance(value, int):
            raise ValueError("Company ID must be an integer.")
        self._company_id = value

    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        if not value or not value.strip():
            raise ValueError("Company name cannot be empty.")
        self._company_name = value.strip()

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        if not value or not value.strip():
            raise ValueError("Location cannot be empty.")
        self._location = value.strip()
