# BLOCKONTROL

- This is a project prototyped by [@berkozdemir](https://twitter.com/berkozdemir), [@memorycollect0r](https://twitter.com/berkozdemir) and [@granulmusic](https://twitter.com/granulmusic), to control devices and softwares in real time with blockchain transactions. The first test has been performed in Kolektif House Maslak at 5th of December, 2021.

# USE CASES

BLOCKONTROL infrastructure can be used for:
- Live performances
- Installations
- Controlling sound, visuals, electronical devices, softwares, HID devices
- Playing a videogame collaboratively and autonomously
- etc.
- Retrospective analysis / replay of a past event

## HOW IT WORKS

- A smart contract has some variables defined in a struct:

```
param_id - "0"
name - "/param"
minVal - 0
maxVal - 999
lastAddress - 0x0000000...
```
- Depending on what is needed, the amount and parameter limits of variables can be adjusted. 

- A local server requests to blockchain via an RPC connection every "n" seconds to get the recent data.

- The server converts the data to OSC messages and sends this to other devices in the local network to interpret.

- A generative music code can change their parameters via these messages, or a light bulb can turn on/off. It is up to you what to do with this.


- It is advised to use testnet for experimentations.

## WHAT CAN BE ADDED?

- A private ERC20 or timer variables can be added in smart contract to add new gamification mechanics (like collect token until someone else changes the variable, and lock the variable with the tokens you spend)

# KOLEKTIF HOUSE PERFORMANCE STUFF

Audience connects to the dapp, changes parameters -> supercollider and touchdesigner gets the data in real time to change the music and visuals

Smart Contract && Sounds: Berk Özdemir
Trombone: Işık Üstündağ
Visuals: İbrahim Sefa Tuna
Web UI and other dev wizardry: Caner Sevince
Stage decoration: Masal Çabuk
Video Documentation: Can Yorar
Graphic design for Blockontrol PDF: Yavuzhan Bora Yiğit

Smart contract: [https://testnet.snowtrace.io/address/0x4ade94ba1ce19ede7caad879a7228f9c000112c5#code](https://testnet.snowtrace.io/address/0x4ade94ba1ce19ede7caad879a7228f9c000112c5#code)

Audio recording: [https://arweave.net/nswjCtk_CWETS6qJ7WyFBnkVmOKhAoLwv98F6OEhmAU](https://arweave.net/nswjCtk_CWETS6qJ7WyFBnkVmOKhAoLwv98F6OEhmAU)

Video teaser: [https://arweave.net/WRuavcja7EjArrpBdlSR0n9nyHN_mfgTEla8R68JTSI](https://arweave.net/WRuavcja7EjArrpBdlSR0n9nyHN_mfgTEla8R68JTSI)
