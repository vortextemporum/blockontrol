import { useWeb3React } from "@web3-react/core"
import Link from "next/link"
import Navbar from "../components/Menu"
import Toast from "../components/Toast";
import useEagerConnect from "../hooks/useEagerConnect";
import { APP_CHAIN_ID, CONTRACT_ADDRESS, switchChain } from "../util";
import { CONTRACT_ABI } from "../contracts/ABI";
import useContract from "../hooks/useContract";

export default function HomePage() {
    const triedToEagerConnect = useEagerConnect();
    const { account, library, chainId } = useWeb3React();
    const contract = useContract(CONTRACT_ADDRESS, CONTRACT_ABI)

    const isConnected = typeof account === "string" && !!library;
    const connect = () => {
        if (!isConnected) {
            console.log('login.');
            // @ts-ignore
            window?.ethereum?.enable()
        }
        if (chainId && chainId !== APP_CHAIN_ID) {
            switchChain()
        }
    }

    return <>
        <Toast contract={contract} />
        <Navbar rightChain={chainId && chainId == APP_CHAIN_ID} isConnected={isConnected} connect={connect} />
        <div className="container">
            <div className="home">
                <p style={{ fontSize: 24 }}>
                    Smart contract controlled internet of things && sounds && images && light && voltage && bits && bytes;
                </p>
                <p>
                    to be used in time based interactive compositions, permanent installations, spatial design, game mechanics, live performances, having an immutable permanent record of events.
                </p>
                <p>
                    A smart contract holds “n” amount of parameters which has a min/max integer range.
                </p>
                <p>
                    <strong>
                        Example:
                    </strong>
                </p>
                <p className="code">
                    {`
                    struct Param { 
                        uint id;
                        uint minVal;
                        uint maxVal;
                        address lastAddress;
                        uint lastChange;
                        uint value;
               }`}
                </p>
                <p>
                    During the performance/installation, wallets can connect to this website and edit any parameters they want.

                    A python script reads the necessary parameters and variables in real time and converts them to “Open Sound Control” messages. Messages are broadcasted to every computer in the local network.
                </p>
                <p className="code">
                    {`
                    /time 329754
                    `}
                </p>

                <p className="code">
                    {`
                    /param [2, 479, '0x5A135de1dB9A1eDc434e661c510B51FC199Fc728', 27033]
                    `}
                </p>

                <p className="code">
                    {`
                    /section [1, 1638124971, 8, '0xFaDdfE36a6677768A5bF8b3593253D2D38b7C702']
                    `}
                </p>
                <p>
                    Any software that can read OSC can parse the incoming data and control anything. Lights in a room, pitch of sine waves, relay controlled electronics, fog machine, modular synth, ram data of a nes game…
                </p>
            </div>
            <div id="#about" className="about">
                <h1>
                    Use case
                </h1>
                <p>
                    Music for smart contract controlled electronics + visuals and instruments
                    Duration: 20-30 minutes
                    <br />

                    8 parameters in contract.
                    <br />
                    <br />
                    Supercollider reads the data for generating sounds / musical phrases - TouchDesigner generates real time visuals. Instruments play alongside.
                    <br />
                </p>
            </div>
            <div id="#team" className="team">
                <h1>
                    TEAM
                </h1>
                <ul className="team-members">
                    <li>
                        <a href="https://twitter.com/berkozdemir" target="_blank" rel="noreferrer">
                            <img src="https://pbs.twimg.com/profile_images/1458250273454018561/7CETcoMd_400x400.jpg" alt="" />
                            <p>
                                BERK
                            </p>
                        </a>
                    </li>
                    <li>
                        <a target="_blank" rel="noreferrer" href="https://twitter.com/memorycollect0r">
                            <img src="https://ipfs.infura.io/ipfs/QmPfXnN7gneZu5eVRcZgwMpmfo2XZhQnzWWbpVsAGktG1x" alt="" />
                            <p>
                                MEMORYCOLLECT0R
                            </p>
                        </a>
                    </li>
                    <li>
                        <a href="https://twitter.com/isefatuna" target="_blank" rel="noreferrer">
                            <img src="https://pbs.twimg.com/profile_images/1377347328353390593/Xl_qM96Y_400x400.jpg" alt="" />
                            <p>
                                ISEFATUNA
                            </p>
                        </a>
                    </li>
                    <li>
                        <a href="https://twitter.com/yborayigit" target="_blank" rel="noreferrer">
                            <img src="https://media.discordapp.net/attachments/443527321799098369/915934787808690226/sacma.png?width=582&height=582" alt="" />
                            <p>
                                YBORAYIGIT
                            </p>
                        </a>
                    </li>
                    <li>
                        <a href="https://twitter.com/masal_cabuk" target="_blank" rel="noreferrer">
                            <img src="https://pbs.twimg.com/profile_images/1452670531841441799/HNG5Rtzu_400x400.jpg" alt="" />
                            <p>
                                PRINCESS HAZEL
                            </p>
                        </a>
                    </li>

                </ul>
            </div>
        </div >
    </>
}
