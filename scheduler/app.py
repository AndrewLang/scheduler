import logging

logging.basicConfig(level=logging.DEBUG)

class Application:

    def run(self):
        logging.info('start application')
        return self
        