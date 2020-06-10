""" Example script to run Mahadiscom library """
from mahadiscom import MahaDiscom


def main():
    mahadiscom = MahaDiscom(cn='123456789246', bun='1111', ct='1')
    billdetails = mahadiscom.get_bill_details()
    print(billdetails['netPPDAmount'])

if __name__ == "__main__":
    main()
