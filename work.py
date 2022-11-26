class Тварини(Живі):
    def дихати(self):
        pass

    def рухатись(self):
        pass

    def харчуватись(self):
        pass
        pass


class Кошеня(Тварини):
    def пити_молоко(self):
      print('П\'ю молочко!')
    def обідати(self):
      self.рухатись()
      print('Я на кухні!')
      self.пити_молоко()