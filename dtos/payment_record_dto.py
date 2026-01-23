class PaymentRecordDto:
    def __init__(self):
        self.id = None
        self.student_id = None
        self.student = None

        self.opened_at = None
        self.due_date = None
        self.paid_at = None

        self.value = None
        self.observation = None
        self.payment_status = None
