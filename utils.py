import Quartz


def get_idle_time():
    idle_time = Quartz.CGEventSourceSecondsSinceLastEventType(
        Quartz.kCGEventSourceStateHIDSystemState, Quartz.kCGAnyInputEventType
    )
    return idle_time
