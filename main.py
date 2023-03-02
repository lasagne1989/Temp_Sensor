import asyncio
from connection import connection
from temp_check import temp_check
from datetime import datetime
import on_off

upper_limit = 18
lower_limit = 17

async def main():
    plugs, sensors = await connection()
    heater = "start"
    while True:
        temp = await temp_check(sensors)
        if temp > upper_limit and heater != "on":
            await on_off.turn_off(plugs)
            heater = "on"
            print("Heater ON!")
        if temp < lower_limit and heater != "off":
            await on_off.turn_on(plugs)
            heater = "off"
            print("Heater OFF!")
        await asyncio.sleep(600)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main())
    loop.run_forever()
