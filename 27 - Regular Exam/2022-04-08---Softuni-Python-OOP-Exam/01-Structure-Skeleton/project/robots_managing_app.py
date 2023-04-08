from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICE_TYPES = {
        'MainService':MainService,
        'SecondaryService':SecondaryService
    }
    VALID_ROBOT_TYPES = {
        "MaleRobot": MaleRobot,
        "FemaleRobot": FemaleRobot
    }

    def __init__(self):
        self.robots = []
        self.services = []


    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICE_TYPES:
            raise Exception("Invalid service type!")
        new_service = self.VALID_SERVICE_TYPES[service_type](name)
        self.services.append(new_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOT_TYPES:
            raise Exception("Invalid robot type!")
        new_robot = self.VALID_ROBOT_TYPES[robot_type](name, kind, price)
        self.robots.append(new_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = [r for r in self.robots if r.name == robot_name][0]
        service = [s for s in self.services if s.name == service_name][0]

        if isinstance(robot, MaleRobot) and not isinstance(service, MainService):
            return "Unsuitable service."
        elif isinstance(robot, FemaleRobot) and not isinstance(service, SecondaryService):
            return "Unsuitable service."

        if len(service.robots)==service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        try:
            robot = [r for r in service.robots if r.name == robot_name][0]
        except IndexError:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)

        return f"Successfully removed {robot_name} from {service_name}."


    def feed_all_robots_from_service(self, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        for robot in service.robots:
            robot.eating()

        number_of_robots_fed = len(service.robots)
        return f"Robots fed: {number_of_robots_fed}."

    def service_price(self, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        total_price = 0
        for robot in service.robots:
            total_price += robot.price

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        service_info = ""
        num_services = len(self.services)
        for i, service in enumerate(self.services):
            info = service.details()
            service_info += info
            if i < num_services - 1:  # add newline only for non-last service
                service_info += "\n"
        return service_info


main_app = RobotsManagingApp()

print(main_app.add_service('SecondaryService', 'ServiceRobotsWorld'))
print(main_app.add_service('MainService', 'ServiceTechnicalsWorld'))
print(main_app.add_robot('FemaleRobot', 'Scrap', 'HouseholdRobots', 321.26))
print(main_app.add_robot('FemaleRobot', 'Sparkle', 'FunnyRobots', 211.11))

print(main_app.add_robot_to_service('Scrap', 'ServiceRobotsWorld'))
print(main_app.add_robot_to_service('Sparkle', 'ServiceRobotsWorld'))

print(main_app.feed_all_robots_from_service('ServiceRobotsWorld'))
print(main_app.feed_all_robots_from_service('ServiceTechnicalsWorld'))

print(main_app.service_price('ServiceRobotsWorld'))
print(main_app.service_price('ServiceTechnicalsWorld'))

print(str(main_app))

print(main_app.remove_robot_from_service('Scrap', 'ServiceRobotsWorld'))
print(main_app.service_price('ServiceRobotsWorld'))
print(main_app.service_price('ServiceTechnicalsWorld'))

print(str(main_app))
