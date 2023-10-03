from uagents import Agent,Context

from dotenv import load_dotenv
from util.getTemp import getTemperature
from util.notify import showNotify
from os import getenv
load_dotenv()  # Load environment variables from .env file




temp_agent = Agent(name="temperature")






@temp_agent.on_interval(period=60.0)
async def interval(ctx:Context):
    started = ctx.storage.get('started')

    if not started:
        #input data 
        location = input("Enter your location : ")
        min_temp = float(input('Minimum temperature(celcius):'))
        max_temp = float(input('Maximum temperature (celcius):'))
        #save in uagents storages
        ctx.storage.set('location',location)
        ctx.storage.set('min_temp',min_temp)
        ctx.storage.set('max_temp',max_temp)
        ctx.storage.set('started',True)
    else:
        ##request api 
        ## send message or email if outside of certain message
        location:str = ctx.storage.get('location')
        min_temp:float = ctx.storage.get('min_temp')
        max_temp:float = ctx.storage.get('max_temp')
        current_temperature =  getTemperature(location=location)
        if current_temperature == -1000:
            showNotify(
                title="Weather api Not working",
                message=f"Perhaps your balance is low"
            )
        elif current_temperature < min_temp:
            showNotify(
                title="Low Temperature",
                message=f"Current Temperature is {current_temperature} less than {min_temp} "
            )
            ctx.logger.info(f'current weather temperature of {location} is less than minimum temperature')
        elif current_temperature > max_temp:
            showNotify(
                title="High Temperature",
                message=f"Current Temperature is {current_temperature} greater than {max_temp} "
            )
            ctx.logger.info(f'current weather temperature of {location} is greater than maximum temperature')
        
        ctx.logger.info(f'current weather temperature = {current_temperature}')


if __name__ == "__main__":
    temp_agent.run()