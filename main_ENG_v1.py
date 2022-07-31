from zeep import Client, Settings
import Client_info
from pprint import pprint
from zeep import helpers
import zeep
import datetime


BARCODE = input('Enter the tracking number to track the shipment: ')

service_url = 'https://tracking.russianpost.ru/rtm34?wsdl'
settings = Settings(strict=False)
client = Client(service_url, settings=settings)

result = client.service.getOperationHistory(
    OperationHistoryRequest={'Barcode': BARCODE, 'MessageType': 0},
    AuthorizationHeader={'login': Client_info.LOGIN, 'password': Client_info.PASSWORD})

#RECORDING BASIC INFORMATION ABOUT THE SENDER, RECIPIENT AND TYPE OF SENDING
sender = result[0]['UserParameters']['Sndr']
send_place = result[0]['AddressParameters']['OperationAddress']['Description']
recipient = result[0]['UserParameters']['Rcpn']
destination_place = result[0]['AddressParameters']['DestinationAddress']['Description']
postal_item = result[0]['ItemParameters']['ComplexItemName']

main_information = {
    'Track number of the shipment': BARCODE,
    'Sender': sender,
    'Shipment place': send_place,
    'Shipment type': postal_item,
    'Recipient': recipient,
    'Destination': destination_place
}
#RECORDING INFORMATION ABOUT THE CURRENT STATUS OF THE SHIPMENT
current_operation = result[-1]['OperationParameters']['OperType']['Name']
current_attribute = result[-1]['OperationParameters']['OperAttr']['Name']
current_operation_place = result[-1]['AddressParameters']['OperationAddress']['Description']
current_operation_date_time = (result[-1]['OperationParameters']['OperDate']).strftime('%m-%d-%Y %H:%M')

current_status = {
    'Last operation': (current_operation, current_attribute),
    'Place of operation': current_operation_place,
    'Date and time of the last operation': current_operation_date_time
}

pprint(main_information)
pprint(current_status)