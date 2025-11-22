from trinity_ai.src.trinity_core import TrinityAI
from eagle_eye.src.eagle_core import EagleEye


def main():
    trinity = TrinityAI()
    eagle = EagleEye()

    # Fake system state & events
    system_state = {"cpu": 0.5, "memory": 0.7}
    raw_events = [{"domain": "system", "message": "all good"}]

    # EAGLE EYE pipeline
    signals = eagle.collect_and_process(raw_events)
    alerts = eagle.detect_anomalies(signals)

    # Pass alerts into TRINITY later (placeholder)
    system_state["alerts"] = alerts

    # TRINITY actions
    trinity.run_maintenance(system_state)
    trinity.run_optimization(system_state)
    trinity.run_security_scan(system_state)


if __name__ == "__main__":
    main()

