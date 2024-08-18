import qrcode
upi_id=input("enter your upi id number")

phonepe=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

phoneqr=qrcode.make(phonepe)
paytmqr=qrcode.make(paytm)
googleqr=qrcode.make(google)

phoneqr.show()
paytmqr.show()
googleqr.show()

