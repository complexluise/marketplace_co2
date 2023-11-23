from enum import Enum


class SheetsDatabase(Enum):
    # Change to CO2 Credits
    PROJECTS = "PROJECTS"
    CO2_CREDITS_PROYECTS = "CO2_CREDITS_PROYECTS"
    CO2_CREDITS_ORDERS = "CO2_CREDITS_ORDERS"


class Proyects(Enum):
    PROJECT_NAME = "Project Name"
    INDUSTRY = "Industry"
    SERIAL_HEADER = "Serial Header"
    LOCATION = "Location"
    DESCRIPTION = "Description"
    SUSTAINABLE_DEVELOPMENT_GOAL = "Sustainable Development Goal"


class CO2CreditsByProject(Enum):
    PROJECT_NAME = "Project Name"
    PROVIDER = "Provider"
    VERIFYING_ENTITY = "Verifying Entity"
    METHODOLOGY = "Methodology"
    CREDITS_GENERATED = "Generated CO2 Credits"
    TON_CO2_EQ = "TON CO2 EQ"
    BUNDLED_CO2_CREDITS = "Bundled CO2 Credits"
    AVAILABLE_CO2_CREDITS = "Available CO2 Credits"
    SERIAL_NUMBER_CO2_CREDITS = "Serial Number CO2 Credits"
    STATUS_BUNDLED = "Status Bundled CO2 Credits"


class CO2CreditsByOrders(Enum):
    BUYERS_NAME = "Buyer's Name"
    PURCHASE_ORDER = "Purchase Order"
    PROJECT_NAME = "Project Name"
    BONDS_PURCHASED = "CO2 Credits Purchased"
    SERIAL_NUMBER = "Serial Number"
    STATUS = "Status"
    COMPENSATION_DESCRIPTION = "Compensation Description"
