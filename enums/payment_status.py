from enum import Enum

class PaymentStatus(Enum):
    OPEN = 'Open'
    PAID = 'Paid'
    OVERDUE = 'Overdue'
    FORGIVEN = 'Forgiven'