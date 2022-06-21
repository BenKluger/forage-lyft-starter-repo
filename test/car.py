from serviceable import Serviceable

class Car(Serviceable):

    def _init_(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
