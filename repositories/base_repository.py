from abc import ABC, abstractmethod
from engine import Session


class BaseRepositoryInterface(ABC):

    @abstractmethod
    def get_all(self):
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id):
        raise NotImplementedError

    @abstractmethod
    def add(self, model):
        raise NotImplementedError

    @abstractmethod
    def update(self, model):
        raise NotImplementedError

    @abstractmethod
    def delete(self, model):
        raise NotImplementedError


class BaseRepository(BaseRepositoryInterface):
    session: Session = None
    model = None

    def __init__(self, session: Session, model):
        self.session = session
        self.model = model

    def get_all(self):
        return self.session.query(self.model).all()

    def get_by_id(self, model_id):
        return self.session.query(self.model).filter(self.model.id == model_id).first()

    def add(self, model):
        self.session.add(model)
        self.session.commit()

    def add_all(self, models: list):
        self.session.add_all(models)
        self.session.commit()

    def update(self, model):
        self.session.commit()

    def delete(self, model):
        self.session.delete(model)
        self.session.commit()
