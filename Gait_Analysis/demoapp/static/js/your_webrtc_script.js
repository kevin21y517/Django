const videoElement = document.getElementById('remoteVideo');
const configuration = { iceServers: [{ urls: 'stun:stun.l.google.com:19302' }] }; // 配置ICE服务器

const peerConnection = new RTCPeerConnection(configuration);

// 处理远程视频流
peerConnection.ontrack = function (event) {
    videoElement.srcObject = event.streams[0];
};

// 处理信令交换等

// 连接到服务器
const socket = new WebSocket('ws://your_server_socket_url');
