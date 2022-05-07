import { useWeb3React } from "@web3-react/core"
import { APP_CHAIN_ID, CONTRACT_ADDRESS, switchChain } from "../util";
import Navbar from "../components/Menu"

export default function About() {
    const { account, library, chainId } = useWeb3React();
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
        <Navbar rightChain={chainId && chainId == APP_CHAIN_ID} isConnected={isConnected} connect={connect} />
        <img className="doc" src="/1920.png" alt="doc" />
    </>
}