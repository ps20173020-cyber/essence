#!/usr/bin/env python3
"""
Main module for Essence project.
"""


def main():
    """Main entry point."""
    print("Hello from Essence!")


def on_forever():
    if input.light_level() > 20:
        servos.P0.set_angle(90)
        pins.digital_write_pin(DigitalPin.P1, 1)
        basic.show_icon(IconNames.HEART)
        basic.pause(1000)
    else:
        servos.P0.set_angle(0)
        pins.digital_write_pin(DigitalPin.P1, 0)
        basic.show_icon(IconNames.NO)
        basic.pause(1000)


if __name__ == "__main__":
    main()
    basic.forever(on_forever)
