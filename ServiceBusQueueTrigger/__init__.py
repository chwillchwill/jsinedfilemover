import logging
import azure.functions as func

def main(msg: func.ServiceBusMessage) -> None:
    logging.info('Python Service Bus queue trigger function processed a message: %s',
                 msg.get_body().decode('utf-8'))