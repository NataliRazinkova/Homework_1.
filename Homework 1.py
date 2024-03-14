from abc import ABC, abstractmethod

class AbstractShow(ABC):
  @abstractmethod
  def get_data(self):
    pass
    
  def show_data(self):
    data = self.get_data()
    print(f'Result: {data}')

class AbstractSearch(ABC):
  @abstractmethod
  def proccess_searching(self):
    pass

  def get_search_term(self):
    self.search_term = input('Enter search param: ')

class BirthdayDisplay(AbstractShow, AbstractSearch):
  def get_data(self):
    return '12/02/23'

  def proccess_searching(self):
    pass

bd = BirthdayDisplay()
bd.get_search_term()

print(f'{bd.show_data()}')