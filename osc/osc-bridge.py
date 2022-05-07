from web3 import Web3

from pythonosc import osc_message_builder
from pythonosc import udp_client
import socket
import time
import sys

w3 = Web3(Web3.HTTPProvider('https://api.avax-test.network/ext/bc/C/rpc'))


address = '0x956cb3c3Db5b3cB13B4Dc7bFE22d1c7f32C71d5C'
abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"time","type":"uint256"}],"name":"musicFinished","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"startTime","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"endTime","type":"uint256"}],"name":"musicStarted","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_parameterId","type":"uint256"},{"indexed":false,"internalType":"address","name":"_sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"_value","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_time","type":"uint256"}],"name":"paramChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_newSection","type":"uint256"},{"indexed":false,"internalType":"address","name":"_sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"_numOfParams","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_time","type":"uint256"}],"name":"sectionChanged","type":"event"},{"inputs":[],"name":"_section","outputs":[{"internalType":"uint256","name":"currentSection","type":"uint256"},{"internalType":"uint256","name":"lastCue","type":"uint256"},{"internalType":"uint256","name":"numParams","type":"uint256"},{"internalType":"address","name":"lastAddress","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_parameter","type":"uint256"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"changeParameter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"value","type":"uint256"}],"internalType":"struct THISSMARTCONTRACTLOVESOSC.ParamChange[]","name":"_input","type":"tuple[]"}],"name":"changeParameterMulti","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"endTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"eventRunning","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"finishMusic","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"finishMusicAdmin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getAllParamStruct","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint256","name":"minVal","type":"uint256"},{"internalType":"uint256","name":"maxVal","type":"uint256"},{"internalType":"address","name":"lastAddress","type":"address"},{"internalType":"uint256","name":"lastChange","type":"uint256"},{"internalType":"uint256","name":"value","type":"uint256"}],"internalType":"struct THISSMARTCONTRACTLOVESOSC.Param[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"musicDuration","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"musicTimeLeft","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"params","outputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint256","name":"minVal","type":"uint256"},{"internalType":"uint256","name":"maxVal","type":"uint256"},{"internalType":"address","name":"lastAddress","type":"address"},{"internalType":"uint256","name":"lastChange","type":"uint256"},{"internalType":"uint256","name":"value","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"showTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"startEvent","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"startTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"}]'

contract_instance = w3.eth.contract(address=address, abi=abi)

calls = [
    {
        "address": address,
        "name": "getAllParamStruct",
        "params": []
    },
    {
        "address": address,
        "name": "showRotationList",
        "params": []
    },
    {
        "address": address,
        "name": "showIdToCanvasLocationList",
        "params": []
    }
]

address_multicall = '0x7991E191193bD3cfCBACA17e16a01F52daab823F'
abi_multicall = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"time","type":"uint256"}],"name":"musicFinished","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"startTime","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"endTime","type":"uint256"}],"name":"musicStarted","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_parameterId","type":"uint256"},{"indexed":false,"internalType":"address","name":"_sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"_value","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_time","type":"uint256"}],"name":"paramChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_newSection","type":"uint256"},{"indexed":false,"internalType":"address","name":"_sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"_numOfParams","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_time","type":"uint256"}],"name":"sectionChanged","type":"event"},{"inputs":[],"name":"_section","outputs":[{"internalType":"uint256","name":"currentSection","type":"uint256"},{"internalType":"uint256","name":"lastCue","type":"uint256"},{"internalType":"uint256","name":"numParams","type":"uint256"},{"internalType":"address","name":"lastAddress","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_parameter","type":"uint256"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"changeParameter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"value","type":"uint256"}],"internalType":"struct THISSMARTCONTRACTLOVESOSC.ParamChange[]","name":"_input","type":"tuple[]"}],"name":"changeParameterMulti","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"endTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"eventRunning","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"finishMusic","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"finishMusicAdmin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getAllParamStruct","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint256","name":"minVal","type":"uint256"},{"internalType":"uint256","name":"maxVal","type":"uint256"},{"internalType":"address","name":"lastAddress","type":"address"},{"internalType":"uint256","name":"lastChange","type":"uint256"},{"internalType":"uint256","name":"value","type":"uint256"}],"internalType":"struct THISSMARTCONTRACTLOVESOSC.Param[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"musicDuration","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"musicTimeLeft","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"params","outputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint256","name":"minVal","type":"uint256"},{"internalType":"uint256","name":"maxVal","type":"uint256"},{"internalType":"address","name":"lastAddress","type":"address"},{"internalType":"uint256","name":"lastChange","type":"uint256"},{"internalType":"uint256","name":"value","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"showTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"startEvent","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"startTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"}]'

multicall_contract_instance = w3.eth.contract(address=address_multicall, abi=abi_multicall)

def main():
    while True:
        paramvalues = contract_instance.functions.getAllParamStruct().call()
        # timePassed = contract_instance.functions.showTime().call()
        # section = contract_instance.functions._section().call()
        # client.send_message("/time", timePassed) 
        # client.send_message("/section", [section[0],section[2],section[1],section[3]]) 

        # print("Broadcasted:", "/time", timePassed)
        # print("section", section)
        print(paramvalues)
        for param in paramvalues:
        #     # OSC PARSING: "/paramname" , "id" , "value" , "lastAddress", "time"
            client.send_message("/param", [ param[0] , param[1], param[6] , param[4], param[5]]) 
            print("Broadcasted:", "/param", [ param[0] , param[1], param[6] , param[4], param[5]])
        time.sleep(3)



if __name__ == '__main__':

    client = udp_client.SimpleUDPClient('127.0.0.1', 4545)
    # client = udp_client.SimpleUDPClient('192.168.0.255', 4545)
    client._sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    sys.exit(main())
