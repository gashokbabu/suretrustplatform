abi = '''[
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_id",
				"type": "address"
			}
		],
		"name": "ai_approved",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address payable",
				"name": "_id",
				"type": "address"
			}
		],
		"name": "application_fee",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "applications",
		"outputs": [
			{
				"internalType": "address payable",
				"name": "id",
				"type": "address"
			},
			{
				"internalType": "address payable",
				"name": "funder",
				"type": "address"
			},
			{
				"internalType": "int256",
				"name": "status",
				"type": "int256"
			},
			{
				"internalType": "uint256",
				"name": "funded_time",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "ending_time",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			},
			{
				"internalType": "int256",
				"name": "annual_inc",
				"type": "int256"
			},
			{
				"internalType": "int256",
				"name": "dti",
				"type": "int256"
			},
			{
				"internalType": "uint256",
				"name": "installment",
				"type": "uint256"
			},
			{
				"internalType": "int256",
				"name": "int_rate",
				"type": "int256"
			},
			{
				"internalType": "int256",
				"name": "revol_bal",
				"type": "int256"
			},
			{
				"internalType": "int256",
				"name": "revol_util",
				"type": "int256"
			},
			{
				"internalType": "int256",
				"name": "total_acc",
				"type": "int256"
			},
			{
				"internalType": "uint256",
				"name": "zip_code",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_name",
				"type": "string"
			},
			{
				"internalType": "int256",
				"name": "_phone",
				"type": "int256"
			},
			{
				"internalType": "uint256",
				"name": "_amount",
				"type": "uint256"
			},
			{
				"internalType": "int256",
				"name": "_annual_inc",
				"type": "int256"
			},
			{
				"internalType": "int256",
				"name": "_dti",
				"type": "int256"
			},
			{
				"internalType": "uint256",
				"name": "_installment",
				"type": "uint256"
			},
			{
				"internalType": "int256",
				"name": "_int_rate",
				"type": "int256"
			},
			{
				"internalType": "int256",
				"name": "_revol_bal",
				"type": "int256"
			},
			{
				"internalType": "int256",
				"name": "_revol_util",
				"type": "int256"
			},
			{
				"internalType": "int256",
				"name": "_total_acc",
				"type": "int256"
			},
			{
				"internalType": "uint256",
				"name": "_zip_code",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "_term",
				"type": "uint256"
			}
		],
		"name": "apply_loan",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address payable",
				"name": "_id",
				"type": "address"
			}
		],
		"name": "fund",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_id",
				"type": "address"
			}
		],
		"name": "get_amount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_id",
				"type": "address"
			}
		],
		"name": "get_applicant_details",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "int256",
				"name": "",
				"type": "int256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_id",
				"type": "address"
			}
		],
		"name": "get_application_details",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "int256",
				"name": "",
				"type": "int256"
			},
			{
				"internalType": "int256",
				"name": "",
				"type": "int256"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "int256",
				"name": "",
				"type": "int256"
			},
			{
				"internalType": "int256",
				"name": "",
				"type": "int256"
			},
			{
				"internalType": "int256",
				"name": "",
				"type": "int256"
			},
			{
				"internalType": "int256",
				"name": "",
				"type": "int256"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_id",
				"type": "address"
			}
		],
		"name": "get_application_status",
		"outputs": [
			{
				"internalType": "int256",
				"name": "",
				"type": "int256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_id",
				"type": "address"
			}
		],
		"name": "get_funder",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_id",
				"type": "address"
			}
		],
		"name": "get_installment",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_id",
				"type": "address"
			}
		],
		"name": "get_last_applied",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "get_owner",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "pure",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_id",
				"type": "address"
			}
		],
		"name": "get_term",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_id",
				"type": "address"
			}
		],
		"name": "get_times_applied",
		"outputs": [
			{
				"internalType": "int256",
				"name": "",
				"type": "int256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_id",
				"type": "address"
			}
		],
		"name": "manual_approve",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_id",
				"type": "address"
			}
		],
		"name": "repay",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "users",
		"outputs": [
			{
				"internalType": "address payable",
				"name": "id",
				"type": "address"
			},
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "int256",
				"name": "phone",
				"type": "int256"
			},
			{
				"internalType": "uint256",
				"name": "remaining_payment",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "last_applied",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "term",
				"type": "uint256"
			},
			{
				"internalType": "int256",
				"name": "n_times_applied",
				"type": "int256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]'''


address = '0x4529dE3F4b78072533369b54F6919D93598A04F0'

HOST = "http://194.195.118.214:8545"

from web3 import Web3
import pickle 
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
import random
import os
import math


w3 = Web3(Web3.HTTPProvider(HOST))

contract = w3.eth.contract(address=address, abi=abi)
import time

account = "0x733f9c6aA7F2B9949797a62FF9FF6Ddb5F55E379"
key = "0x181d9f1d8bf046a48ef27c79fe6b075ba585b2d38f3bd60a69d522b8fb02eebe"





def apply_loan(account,key,name,phone,amount,annual_inc,dti,installment,int_rate,revol_bal,revol_util,total_acc,zip_code,term):
	
	try:
		name = str(name)
		phone = int(phone)
		amount = int(amount)
		annual_inc = int(annual_inc)
		dti = int(dti)
		installment = int(installment)
		int_rate = int(int_rate)
		revol_bal = int(revol_bal)
		revol_util = int(revol_util)
		total_acc = int(total_acc)
		zip_code = int(zip_code)
		term = int(term)
	except:
		return "Give right inputs"
	transaction = contract.functions.apply_loan(name,phone,amount,annual_inc,dti,installment,int_rate,revol_bal,revol_util,total_acc,zip_code,term).buildTransaction({'gas': 700000,'gasPrice': w3.toWei('1', 'gwei'),'from': account,'nonce': w3.eth.getTransactionCount(account)})
	private_key = key
	signed_txn = w3.eth.account.signTransaction(transaction, private_key=private_key)
	hexinfo = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

	
	time.sleep(100)

	rich_logs = contract.functions.get_applicant_details(account).call()
	if rich_logs[0] == name:
		return "sucessfully applied for loan.."
	return "Please pass right inputs, transaction failed..."

def fund(account,key,application_id,amount):
	pre_balance = w3.eth.getBalance(application_id)

	transaction = contract.functions.fund(application_id).buildTransaction({'gas': 700000,'gasPrice': w3.toWei('1', 'gwei'),'from': account,'value':amount,'nonce': w3.eth.getTransactionCount(account)})
	signed_txn = w3.eth.account.signTransaction(transaction, private_key=key)
	hexinfo = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
	time.sleep(100)
	post_balance = w3.eth.getBalance(application_id)

	if post_balance > pre_balance:
		return "application funded.."
	return "Oops! please intiate funding process again,"


def application_fee(user):
	account = "0x8b6d86022a9fc5a96e825ef5a0d464b041b14b76"
	key = "0x47c7b529adddd345df113fe8d75fa03f468983ca38fc6e8a02e0f389e27bfad8"
	transaction = contract.functions.application_fee(user).buildTransaction({'gas': 700000,'gasPrice': w3.toWei('1', 'gwei'),'from': account,'value':10000000000000000000,'nonce': w3.eth.getTransactionCount(account)})
	signed_txn = w3.eth.account.signTransaction(transaction, private_key=key)
	hexinfo = w3.eth.sendRawTransaction(signed_txn.rawTransaction)



def repay(account,key,application_id,amount):


	transaction = contract.functions.fund(application_id).buildTransaction({'gas': 700000,'gasPrice': w3.toWei('1', 'gwei'),'from': account,'value':amount,'nonce': w3.eth.getTransactionCount(account)})
	signed_txn = w3.eth.account.signTransaction(transaction, private_key=key)
	hexinfo = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
	time.sleep(100)
	return str(get_amount(application_id)) + "amount is still need to be paid"

def manual_approve(account,key,application_id):
	transaction = contract.functions.fund(application_id).buildTransaction({'gas': 700000,'gasPrice': w3.toWei('1', 'gwei'),'from': account,'value':amount,'nonce': w3.eth.getTransactionCount(account)})
	signed_txn = w3.eth.account.signTransaction(transaction, private_key=key)
	hexinfo = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
	time.sleep(100)
	return "please check if loan is approved..."

def get_applicant_details(applicant_id):
	return contract.functions.get_applicant_details(applicant_id).call()

def get_application_details(applicant_id):
	return contract.functions.get_application_details(applicant_id).call()

def get_application_status(applicant_id):
	return contract.functions.get_application_status(applicant_id).call()

def get_funder(applicant_id):
	return contract.functions.get_funder(applicant_id).call()

def get_installment(applicant_id):
	return contract.functions.get_installments(applicant_id).call()

def get_amount(applicant_id):
	return contract.functions.get_amount(applicant_id).call()

def get_term(applicant_id):
	return contract.functions.get_application_details(applicant_id).call()

def get_last_applied(applicant_id):
	return contract.functions.get_application_details(applicant_id).call()

def get_n_times_applied(applicant_id):
	return contract.functions.get_n_times_applied(applicant_id).call()




#results = apply_loan(account,key,'test',1,2,3,4,5,6,7,8,9,0,10)
#print(results)



