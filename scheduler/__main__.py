from scheduler.app import Application
import logging

logging.basicConfig(level=logging.DEBUG)

print('starting...')

if __name__ == '__main__':
    logging.info('Start scheduler')
    app = Application()
    app.run()
    
