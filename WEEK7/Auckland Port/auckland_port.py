from abc import ABC, abstractmethod

class EventLog:
    def __init__(self):
        self.events = []
    def log(self, msg):
        print(msg)
        self.events.append(msg)

# Singleton pattern: ensures only one PortOperationsCenter exists
class PortOperationsCenter:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._init_once()
        return cls._instance
    def _init_once(self):
        self.vehicle_id_counter = 1000
        self.log = EventLog()
    def next_vehicle_id(self):
        vid = self.vehicle_id_counter
        self.vehicle_id_counter += 1
        return vid

class Cargo:
    def __init__(self, description, weight):
        self.description = description
        self.weight = weight

class ShipmentOrder:
    def __init__(self, order_id, mode, cargo):
        self.order_id = order_id
        self.mode = mode  # 'road', 'sea', or 'rail'
        self.cargo = cargo

class Transport(ABC):
    def __init__(self, shipment_order):
        self.shipment_order = shipment_order
        self.center = PortOperationsCenter()
        self.vehicle_id = self.center.next_vehicle_id()
    @abstractmethod
    def transport(self):
        pass

class RoadTruck(Transport):
    def transport(self):
        self.center.log.log(
            f"Truck {self.vehicle_id} transported cargo '{self.shipment_order.cargo.description}' "
            f"({self.shipment_order.cargo.weight} kg) for order {self.shipment_order.order_id}."
        )

class SeaBarge(Transport):
    def transport(self):
        self.center.log.log(
            f"Barge {self.vehicle_id} docked cargo '{self.shipment_order.cargo.description}' "
            f"({self.shipment_order.cargo.weight} kg) for order {self.shipment_order.order_id}."
        )

class Train(Transport):
    def transport(self):
        self.center.log.log(
            f"Train {self.vehicle_id} transported cargo '{self.shipment_order.cargo.description}' "
            f"({self.shipment_order.cargo.weight} kg) for order {self.shipment_order.order_id}."
        )

# Factory pattern: creates transport objects based on shipment mode
class TransportFactory:
    _mode_map = {
        'road': RoadTruck,
        'sea': SeaBarge,
        'rail': Train
    }
    @staticmethod
    def create(shipment_order):
        cls = TransportFactory._mode_map.get(shipment_order.mode)
        if cls:
            return cls(shipment_order)
        else:
            raise ValueError('Unknown mode')

def main():
    center = PortOperationsCenter()
    print("Auckland Port Logistics - Simple Shipment Entry\n")
    mode = input("Enter mode (road/sea/rail): ").strip().lower()
    if mode not in ('road', 'sea', 'rail'):
        print("Invalid mode. Exiting.")
        return
    desc = input("Enter cargo description: ").strip()
    try:
        weight = float(input("Enter cargo weight (kg): "))
    except ValueError:
        print("Invalid weight. Exiting.")
        return
    cargo = Cargo(desc, weight)
    order = ShipmentOrder(1, mode, cargo)
    t = TransportFactory.create(order)
    t.transport()
    print("\nEvent Log:")
    for e in center.log.events:
        print(e)

if __name__ == "__main__":
    main()
