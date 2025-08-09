import tabsdata as td
import os
from tabsdata.api.tabsdata_server import TabsdataServer
import inspect
import sys
import re



def cancel_flows():
    server = TabsdataServer("127.0.0.1:2457", "admin", "tabsdata", "sys_admin")
    transactions = server.list_transactions()
    stalled_transactions = [i for i in transactions if i.status == 'Stalled']
    if len(stalled_transactions) > 0:
        canceled_transactions = [i.cancel() for i in stalled_transactions]
        return canceled_transactions
    return 'No Stalled Transactions Found'
