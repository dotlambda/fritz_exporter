from defusedxml import ElementTree


def parse_aha_device_xml(deviceinfo: str) -> dict[str, str]:
    device: ElementTree = ElementTree.fromstring(deviceinfo)

    battery_level = device.find("battery")
    battery_low = device.find("batterylow")

    result = {}

    if battery_level is not None:
        result["battery_level"] = battery_level.text

    if battery_low is not None:
        result["battery_low"] = battery_low.text

    return result
