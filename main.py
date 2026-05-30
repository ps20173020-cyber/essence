#!/usr/bin/env python3
"""
Main module for Essence project.
"""


def main():
    """Main entry point."""
    print("Hello from Essence!")


def on_forever():
    value_of_soil_moisture_0100_at_pin_P1 = 0
    if value_of_soil_moisture_0100_at_pin_P1 < 50:
        servos.P0.set_angle(90)
        pins.digital_write_pin(DigitalPin.P2, 0)
        basic.show_icon(IconNames.HEART)
        basic.pause(1000)
    else:
        servos.P0.set_angle(0)
        pins.digital_write_pin(DigitalPin.P2, 1)
        basic.show_icon(IconNames.NO)
        basic.pause(1000)


if __name__ == "__main__":
    main()
    basic.forever(on_forever)
