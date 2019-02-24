import requests

# fetch data from  API
response = requests.get("https://bitbay.net/API/Public/BTCPLN/ticker.json")
data = response.json()
best_bid=data['bid']
best_ask=data['ask']
print('bid:',best_bid,'ask:',best_ask)

#TASKS (11p)
#To use the requests library you have to install it first. If you have pip and you're using python3 interpreter in your project
# then simply pip3 install requests

# 1 Find another public API with cryptocurrency and compare prices. As an output print:
# "Currently the XXX exchange market is better for buying whilst YYY is better for selling" (3p)
# 2 Use https://randomuser.me API to download a random user data.
# Create and store 100 random users with ids, username, name (first + last name) using this API (2p)
# 3 Prepare a simulation of transactions between these users
# Take random user and pair him/her with another one. Assume a random amount but take real world price. Sum up the transaction printing:
# username1 exchanged X.XXX BTC with username2 for PLN YYYYY.YYY PLN. (2p)
# Simulate real time - do not proceed all transactions at once. Try to make around 100 transactions per minute (2p)
# Simulate user's assets. Creating a user assign random amount of a given currency. Take it into account while performing a transaction.
# Remember to amend user's assets after the transaction. (2p)