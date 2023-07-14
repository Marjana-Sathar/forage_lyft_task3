from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery
from car import Car
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.nubbin_battery import NubbinBattery
def CarFactory():
    @staticmethod
    def create_calliope(current_milage,last_service_milage,current_date,last_service_date):
        engine=CapuletEngine(current_milage,last_service_milage)
        battery=SpindlerBattery(last_service_date,current_date)
        car=Car(engine,battery)
        return car
    @staticmethod
    def create_glissade(current_milage,last_service_milage,current_date,last_service_date):
        engine=WilloughbyEngine(current_milage, last_service_milage)
        battery=SpindlerBattery(last_service_date,current_date)
        car=Car(engine,battery)
        return car
    @staticmethod
    def create_pallindrome(warning_light_on,current_date,last_service_date):
        engine=SternmanEngine(warning_light_on)
        battery=SpindlerBattery(last_service_date,current_date)
        car=Car(engine,battery)
        return car
    @staticmethod
    def create_rorschach(current_milage,last_service_milage,current_date,last_service_date):
        engine=WilloughbyEngine(current_milage,last_service_milage)
        battery=NubbinBattery(last_service_date,current_date)
        car=Car(engine,battery)
        return car
    @staticmethod
    def create_rorschach(current_milage,last_service_milage,current_date,last_service_date):
        engine=CapuletEngine(current_milage,last_service_milage)
        battery=NubbinBattery(last_service_date,current_date)
        car=Car(engine,battery)
        return car