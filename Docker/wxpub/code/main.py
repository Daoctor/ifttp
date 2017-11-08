#!/usr/bin/env python
#!coding=utf8
import werobot

config = {
    "token":"",
    "HOST": "0.0.0.0",
    "PORT":4001,
    "APP_ID":"",
    "ENCODING_AES_KEY":"",
    # "APP_SECRET":"",
}

robot = werobot.WeRoBot(**config)

@robot.text
def hello_world(message):
    return message.content


if __name__ == "__main__":
    robot.run()