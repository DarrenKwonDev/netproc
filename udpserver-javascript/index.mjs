import dgram from "dgram";

const PORT = 5500;
const LO = "127.0.0.1";

const socket = dgram.createSocket("udp4");

socket.bind(PORT, LO);
socket.on("message", (msg, info) => {
    // interface RemoteInfo {
    //     address: string;
    //     family: 'IPv4' | 'IPv6';
    //     port: number;
    //     size: number;
    // }
    console.log(
        `My Server got a datagram ${msg}, from: ${info.address}:${info.port}`
    );
});
