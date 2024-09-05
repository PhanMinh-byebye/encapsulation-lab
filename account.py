class Account:
    def __inti__(self,id, balance, pin):
        self.id = id
        self.balance = balance
        self.pin = pin
    def get_id(self, pin, id):
        if self.pin == pin:
            return self.id
        else:
            return "wrong pin"
    def change_pin(old_pin, new_pin, self):
        if old_pin == self.pin:
            self.pin == new_pin
            return "pin changed"
        else:
            return "wrong pin"


