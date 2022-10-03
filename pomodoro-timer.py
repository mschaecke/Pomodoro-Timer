#!/usr/bin/env python
# -*-coding:utf-8 -*-

""" A simple Pomodoro timer.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Marvin Alexander Schäcke"
__contact__ = "@mschaecke on GitHub"
__copyright__ = "Copyright 2022"
__date__ = "2022/10/02"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "Production"
__version__ = "1.0"


import time


# Variables

greetings_message = """
Thank you for using my Pomodoro timer! 
You can stop the timer by closing the terminal or pressing Control+C."""

work_input_message = """
How long would you like to work (in minutes)? """

break_input_message = """
How long should your break be (in minutes)? """

input_error_message = """
The input did not work. 
Please enter a number greater than or equal to 0: """

wait_work_message = """
Press Enter to start the work interval. """

start_work_message = """Starting work interval."""

end_work_message = """
Well done! It's time for a break!"""

wait_break_message = """
Press Enter to start the break interval. """

start_break_message = """Starting break interval."""

end_break_message = """
The break is over! Time to get back to work!"""


# Functions

def convert_to_float(string_input: str) -> float:
    string_input = string_input.strip(' \n\t').replace(",", ".")
    try:
        return float(string_input)
    except ValueError:
        return -1.0


def is_valid_input(minutes: float) -> bool:
    if isinstance(minutes, float) and minutes >= 0:
        return True
    return False


def start_input_loop() -> float:
    minutes = convert_to_float(input())

    while not is_valid_input(minutes):
        print(input_error_message)
        minutes = convert_to_float(input())

    return minutes


def print_progress_bar(minutes: float):
    finished_icon = "X"
    not_finished_icon = "_"
    minutes_in_seconds = minutes * 60

    for i in range(0, 11):
        print(f"|{finished_icon * i}{not_finished_icon*(10-i)}| {i}0%")
        if i < 10:
            time.sleep(minutes_in_seconds / 10)


# Main

if __name__ == '__main__':
    print(greetings_message)
    print(work_input_message)
    work_minutes = start_input_loop()
    print(break_input_message)
    break_minutes = start_input_loop()

    while True:
        print(wait_work_message)
        input()
        print(start_work_message)
        print_progress_bar(work_minutes)
        print(end_work_message)

        print(wait_break_message)
        input()
        print(start_break_message)
        print_progress_bar(break_minutes)
        print(end_break_message)
