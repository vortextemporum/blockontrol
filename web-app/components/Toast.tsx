import { useEffect } from 'react';
import { ToastContainer, toast } from 'react-toastify';
import { shortenHex } from '../util';
export default function Toast({ contract }) {

    function useToast(id, sender, value, time) {
        console.log(time);
        toast(`${shortenHex(sender, 4)} just changed Parameter ${parseInt(id)} to ${parseInt(value)}. -${new Date().toLocaleDateString()} - ${new Date().toLocaleTimeString()}`, {
            autoClose: 3000
        })
    }

    useEffect(() => {
        if (contract) {
            contract?.on('paramChanged', useToast)
        } return () => {
            contract?.off('paramChanged', useToast)
        }
    }, [contract])
    return (
        <div>
            <ToastContainer />
        </div>
    );
}