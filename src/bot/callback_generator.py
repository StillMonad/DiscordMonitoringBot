from loguru import logger
from functools import partial
import os

class CallbackGenerator:
    @staticmethod
    def bind(bind_to):
        """
        Adding methods from classes in /callbacks folder to given class
        """
        CallbackGenerator.__scope_subclasses()
        avoid = ['bind', 'scope_subclasses']
        for child in CallbackGenerator.__subclasses__():
            callback_names = [method for method in dir(child) if not method.startswith('__')]
            for callback_name in callback_names:
                if any(a in callback_name for a in avoid):
                    continue
                callback = getattr(child, callback_name)
                logger.info("Binding callback " + callback_name)
                modified_callback = partial(callback, bind_to)
                setattr(bind_to, callback.__name__, modified_callback)

    @staticmethod
    def __scope_subclasses():
        """
        importing all modules from /callback folder

        __subclasses__ is not working, if subclasses are not loaded into scope
        """
        path = os.path.join('src', 'bot', 'callbacks', '')
        for module in os.listdir(os.path.dirname(path)):
            if module == "__pycache__":
                continue
            module = module[:-3]
            exec(f'import src.bot.callbacks.{module}')