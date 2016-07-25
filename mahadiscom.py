import requests
import json


class MahaDiscom(object):
    """ Class to get details about Mahadiscom """
    def __init__(self, cn, bun, ct):
        """ __init__ """
        self.serverurl = 'https://wss.mahadiscom.in/wss/'
        self.con_details = {}
        self.con_details['ConsumerNo'] = cn
        self.con_details['BuNumber'] = bun
        self.con_details['consumerType'] = ct

    def is_consumer_valid(self):
        """
        Helper function to check if consumer is valid or not
        returns : True if consumer is valid
                  False if consumer is not valid
        """
        actionurl = 'wss?uiActionName=validateConsumerNumberHTLT&IsAjax=true'
        url = self.serverurl + actionurl
        response = requests.post(url, data=self.con_details)
        if response.status_code != 200:
            return False
        elif response.text == 'false':
            return False
        elif response.text == 'true':
            return True

    def get_bill_details(self):
        """
        Function to get bill details
        returns : a dictionary with consumer's bill details
        """
        billdetails = {}
        actionurl = "wss?uiActionName=postViewPayBill&IsAjax=true"
        url = self.serverurl + actionurl
        response = requests.post(url, data=self.con_details)
        try:
            billdetails = json.loads(response.text)
        except ValueError as err:
            print("Unable to parse json response" + str(err))

        if response.status_code == 200:
            return billdetails
        else:
            print("ERROR: Return code is Non-2xx : %d" % response.status_code)
            return {}
