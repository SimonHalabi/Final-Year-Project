from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from typing import Dict, Text, Any, List

import requests
from rasa_sdk import Action
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.forms import FormAction

import xlrd


def _find_sheep_position() -> List[Dict]:

    file_name = "data_pipeline.xlsx"
    workbook = xlrd.open_workbook(file_name)
    sheet = workbook.sheet_by_index(0)
    sheep_position = sheet.cell_value(1, 0)

    return sheep_position


class FindSheepPosition(Action):

    def name(self) -> Text:

        return "find_sheep_position"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        return [SlotSet("sheep_position", _find_sheep_position())]


class SheepPositionForm(FormAction):

    def name(self) -> Text:

        return "sheep_position_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        return "sheep_position"

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"sheep_position": self.from_entity(entity="sheep_position",
                                                   intent="sheep_position")}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:

        sheep_position = tracker.get_slot('sheep_position')

        results = _find_sheep_position()
        if len(results) == 0:
            dispatcher.utter_message("Sorry, not found!")
            return []

        return [SlotSet("sheep_position", _find_sheep_position())]


def _find_sheep_velocity() -> List[Dict]:

    file_name = "data_pipeline.xlsx"
    workbook = xlrd.open_workbook(file_name)
    sheet = workbook.sheet_by_index(0)
    sheep_velocity = sheet.cell_value(1, 1)

    return sheep_velocity


class FindSheepVelocity(Action):

    def name(self) -> Text:
        return "find_sheep_velocity"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:
        return [SlotSet("sheep_velocity", _find_sheep_velocity())]


class SheepVelocityForm(FormAction):

    def name(self) -> Text:
        return "sheep_velocity_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return "sheep_velocity"

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"sheep_velocity": self.from_entity(entity="sheep_velocity",
                                                   intent="sheep_velocity")}

    def submit(self,
                dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]
                ) -> List[Dict]:
        sheep_velocity = tracker.get_slot('sheep_velocity')

        results = _find_sheep_velocity()
        if len(results) == 0:
            dispatcher.utter_message("Sorry, not found!")
            return []

        return [SlotSet("sheep_velocity", _find_sheep_velocity())]


def _find_drone_position() -> List[Dict]:

    file_name = "data_pipeline.xlsx"
    workbook = xlrd.open_workbook(file_name)
    sheet = workbook.sheet_by_index(0)
    drone_position = sheet.cell_value(1, 2)

    return drone_position


class FindDronePosition(Action):

    def name(self) -> Text:
        return "find_drone_position"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:
        return [SlotSet("drone_position", _find_drone_position())]


class DronePositionForm(FormAction):

    def name(self) -> Text:
        return "drone_position_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return "drone_position"

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"drone_position": self.from_entity(entity="drone_position",
                                                   intent="drone_position")}

    def submit(self,
                dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]
                ) -> List[Dict]:
        drone_position = tracker.get_slot('drone_position')

        results = _find_drone_position()
        if len(results) == 0:
            dispatcher.utter_message("Sorry, not found!")
            return []

        return [SlotSet("drone_position", _find_drone_position())]


def _find_drone_velocity() -> List[Dict]:

    file_name = "data_pipeline.xlsx"
    workbook = xlrd.open_workbook(file_name)
    sheet = workbook.sheet_by_index(0)
    drone_velocity = sheet.cell_value(1, 3)

    return drone_velocity


class FindDroneVelocity(Action):

    def name(self) -> Text:
        return "find_drone_velocity"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:
        return [SlotSet("drone_velocity", _find_drone_velocity())]


class DroneVelocityForm(FormAction):

    def name(self) -> Text:
        return "drone_velocity_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return "drone_velocity"

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"drone_velocity": self.from_entity(entity="drone_velocity",
                                                   intent="drone_velocity")}

    def submit(self,
                dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]
                ) -> List[Dict]:
        drone_velocity = tracker.get_slot('drone_velocity')

        results = _find_drone_velocity()
        if len(results) == 0:
            dispatcher.utter_message("Sorry, not found!")
            return []

        return [SlotSet("drone_velocity", _find_drone_velocity())]


def _find_drone_battery() -> List[Dict]:

    file_name = "data_pipeline.xlsx"
    workbook = xlrd.open_workbook(file_name)
    sheet = workbook.sheet_by_index(0)
    drone_battery = sheet.cell_value(1, 4)

    return drone_battery


class FindDroneBattery(Action):

    def name(self) -> Text:
        return "find_drone_battery"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:
        return [SlotSet("drone_battery", _find_drone_battery())]


class DroneBatteryForm(FormAction):

    def name(self) -> Text:
        return "drone_battery_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return "drone_battery"

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"drone_battery": self.from_entity(entity="drone_battery",
                                                   intent="drone_battery")}

    def submit(self,
                dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]
                ) -> List[Dict]:
        drone_velocity = tracker.get_slot('drone_battery')

        results = _find_drone_battery()
        if len(results) == 0:
            dispatcher.utter_message("Sorry, not found!")
            return []

        return [SlotSet("drone_battery", _find_drone_battery())]


def _find_drone_actions() -> List[Dict]:

    file_name = "data_pipeline.xlsx"
    workbook = xlrd.open_workbook(file_name)
    sheet = workbook.sheet_by_index(0)
    drone_actions = sheet.cell_value(1, 5)

    return drone_actions


class FindDroneActions(Action):

    def name(self) -> Text:
        return "find_drone_actions"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:
        return [SlotSet("drone_actions", _find_drone_actions())]


class DroneActionsForm(FormAction):

    def name(self) -> Text:
        return "drone_actions_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return "drone_actions"

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"drone_actions": self.from_entity(entity="drone_actions",
                                                   intent="drone_actions")}

    def submit(self,
                dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]
                ) -> List[Dict]:
        drone_actions = tracker.get_slot('drone_actions')

        results = _find_drone_actions()
        if len(results) == 0:
            dispatcher.utter_message("Sorry, not found!")
            return []

        return [SlotSet("drone_actions", _find_drone_actions())]


def _find_sheep_psych() -> List[Dict]:

    file_name = "data_pipeline.xlsx"
    workbook = xlrd.open_workbook(file_name)
    sheet = workbook.sheet_by_index(0)
    sheep_psych = sheet.cell_value(1, 6)

    return sheep_psych


class FindSheepPsych(Action):

    def name(self) -> Text:
        return "find_sheep_psych"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:
        return [SlotSet("sheep_psych", _find_sheep_psych())]


class SheepPsychForm(FormAction):

    def name(self) -> Text:
        return "sheep_psych_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return "sheep_psych"

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"sheep_psych": self.from_entity(entity="sheep_psych",
                                                   intent="sheep_psych")}

    def submit(self,
                dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]
                ) -> List[Dict]:
        sheep_psych = tracker.get_slot('sheep_psych')

        results = _find_sheep_psych()
        if len(results) == 0:
            dispatcher.utter_message("Sorry, not found!")
            return []

        return [SlotSet("sheep_psych", _find_sheep_psych())]


def _find_drone_sheep_dynamic() -> List[Dict]:

    file_name = "data_pipeline.xlsx"
    workbook = xlrd.open_workbook(file_name)
    sheet = workbook.sheet_by_index(0)
    drone_sheep_dynamic = sheet.cell_value(1, 7)

    return drone_sheep_dynamic


class FindDroneSheepDynamic(Action):

    def name(self) -> Text:
        return "find_drone_sheep_dynamic"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:
        return [SlotSet("drone_sheep_dynamic", _find_drone_sheep_dynamic())]


class DroneSheepDynamicForm(FormAction):

    def name(self) -> Text:
        return "drone_sheep_dynamic_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return "drone_sheep_dynamic"

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"drone_sheep_dynamic": self.from_entity(entity="drone_sheep_dynamic",
                                                   intent="drone_sheep_dynamic")}

    def submit(self,
                dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]
                ) -> List[Dict]:
        drone_sheep_dynamic = tracker.get_slot('drone_sheep_dynamic')

        results = _find_drone_sheep_dynamic()
        if len(results) == 0:
            dispatcher.utter_message("Sorry, not found!")
            return []

        return [SlotSet("drone_sheep_dynamic", _find_drone_sheep_dynamic())]


def _find_sheep_sheep_dynamic() -> List[Dict]:

    file_name = "data_pipeline.xlsx"
    workbook = xlrd.open_workbook(file_name)
    sheet = workbook.sheet_by_index(0)
    sheep_sheep_dynamic = sheet.cell_value(1, 8)

    return sheep_sheep_dynamic


class FindSheepSheepDynamic(Action):

    def name(self) -> Text:
        return "find_sheep_sheep_dynamic"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:
        return [SlotSet("sheep_sheep_dynamic", _find_sheep_sheep_dynamic())]


class SheepSheepDynamicForm(FormAction):

    def name(self) -> Text:
        return "sheep_sheep_dynamic_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return "sheep_sheep_dynamic"

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"sheep_sheep_dynamic": self.from_entity(entity="sheep_sheep_dynamic",
                                                   intent="sheep_sheep_dynamic")}

    def submit(self,
                dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]
                ) -> List[Dict]:
        sheep_sheep_dynamic = tracker.get_slot('sheep_sheep_dynamic')

        results = _find_sheep_sheep_dynamic()
        if len(results) == 0:
            dispatcher.utter_message("Sorry, not found!")
            return []

        return [SlotSet("sheep_sheep_dynamic", _find_sheep_sheep_dynamic())]


def _find_human_drone_dynamic() -> List[Dict]:

    file_name = "data_pipeline.xlsx"
    workbook = xlrd.open_workbook(file_name)
    sheet = workbook.sheet_by_index(0)
    human_drone_dynamic = sheet.cell_value(1, 9)

    return human_drone_dynamic


class FindHumanDroneDynamic(Action):

    def name(self) -> Text:
        return "find_human_drone_dynamic"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:
        return [SlotSet("human_drone_dynamic", _find_human_drone_dynamic())]


class HumanDroneDynamicForm(FormAction):

    def name(self) -> Text:
        return "human_drone_dynamic_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return "human_drone_dynamic"

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"human_drone_dynamic": self.from_entity(entity="human_drone_dynamic",
                                                   intent="human_drone_dynamic")}

    def submit(self,
                dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]
                ) -> List[Dict]:
        human_drone_dynamic = tracker.get_slot('human_drone_dynamic')

        results = _find_human_drone_dynamic()
        if len(results) == 0:
            dispatcher.utter_message("Sorry, not found!")
            return []

        return [SlotSet("human_drone_dynamic", _find_human_drone_dynamic())]


def _find_drone_altitude() -> List[Dict]:

    file_name = "data_pipeline.xlsx"
    workbook = xlrd.open_workbook(file_name)
    sheet = workbook.sheet_by_index(0)
    drone_altitude = sheet.cell_value(1, 10)

    return drone_altitude


class FindDroneAltitude(Action):

    def name(self) -> Text:
        return "find_drone_altitude"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:
        return [SlotSet("drone_altitude", _find_drone_altitude())]


class DroneAltitudeForm(FormAction):

    def name(self) -> Text:
        return "drone_altitude_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return "drone_altitude"

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"drone_altitude": self.from_entity(entity="drone_altitude",
                                                   intent="drone_altitude")}

    def submit(self,
                dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]
                ) -> List[Dict]:
        drone_altitude = tracker.get_slot('drone_altitude')

        results = _find_drone_altitude()
        if len(results) == 0:
            dispatcher.utter_message("Sorry, not found!")
            return []

        return [SlotSet("drone_altitude", _find_drone_altitude())]