import { Web3ReactProvider } from "@web3-react/core";
import type { AppProps } from "next/app";
import getLibrary from "../getLibrary";
import "../styles/globals.scss";
import 'react-toastify/dist/ReactToastify.css';
import Head from "next/dist/shared/lib/head";
function NextWeb3App({ Component, pageProps }: AppProps) {
  return (
    <Web3ReactProvider getLibrary={getLibrary}>
      <Head>
        <title>
          AvalancheHacks - CONTROLLER FOR SMART CONTRACT CONTROLLED LIVE ELECTRONICS / SMART DEVICES
        </title>
      </Head>
      <Component {...pageProps} />
    </Web3ReactProvider>
  );
}

export default NextWeb3App;
