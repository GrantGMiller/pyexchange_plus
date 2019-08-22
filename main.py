import pyexchange_plus as pyexchange
from pytz import timezone
import datetime
import creds

URL = 'https://outlook.office365.com/EWS/Exchange.asmx'


def GetTokenFromOauthService():
    # this parts on you bruh
    return 'secret_access_token'


access_token = GetTokenFromOauthService()

connection = pyexchange.ExchangeOauthConnection(
    url=URL,
    access_token=access_token,
)

exchange = pyexchange.Office365Service(connection)

nowDT = datetime.datetime.utcnow()
startDT = timezone("US/Eastern").localize(nowDT)
endDT = timezone("US/Eastern").localize(nowDT + datetime.timedelta(days=1))

print('startDT=', startDT)
print('endDT=', endDT)

callist = exchange.calendar(creds.username).list_events(
    start=startDT,
    end=endDT,
    details=True
)
# make a basic HTML table to display the calendar info
html = '<table border="1"><tr><th>Start (UTC)</th><th>End (UTC)</th><th>Subject</th></tr>'
for event in callist.events:
    html += '<tr>'
    html += "<td>{}</td>".format(event.start)
    html += "<td>{}</td>".format(event.end)
    html += "<td>{}</td>".format(event.subject)
    html += '</tr>'
print('events=', html)
print(html)
