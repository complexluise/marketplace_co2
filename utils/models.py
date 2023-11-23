from enum import Enum


class SheetsDatabase(Enum):
    # Change to CO2 Credits
    PROJECTS = "Proyectos"  # -> PROJECTS
    PROJECTS_BONUS = "Bonos_Proyecto"  # -> CO2_CREDITS_PROYECTS
    ORDER_BONUS = "Ordeners_Bonos"  # -> CO2_CREDITS_ORDERS


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
    CREDITS_GENERATED = "Number of Credits Generated"
    TON_CO2_EQ = "TON CO2 EQ"
    CREDITS_IN_PACKAGES = "Credits in Packages"
    AVAILABLE_CREDITS = "Available Credits"
    SERIAL_NUMBER_CREDITS = "Serial Number of Credits"
    STATUS = "Status"


class CO2CreditsByOrders(Enum):
    BUYERS_NAME = "Buyers Name"
    PURCHASE_ORDER = "Purchase Order"
    PROJECT_NAME = "Project Name"
    BONDS_PURCHASED = "Bonds Purchased"  # TODO Update to CO2 Credits Purchased
    SERIAL_NUMBER = "Serial Number"
    STATUS = "Status"
    COMPENSATION_DESCRIPTION = "Compensation Description"
