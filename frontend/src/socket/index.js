import { reactive } from 'vue';
import { io } from 'socket.io-client';
import { throttle } from 'throttle-debounce';

export const state = reactive({
    connected: false,
});

export const socket = io(import.meta.env.VITE_SOCKETIO_SERVER);

socket.on('connect', () => {
    state.connected = true;
    socket.emit('connection', { data: 'Client connected!' });
});

socket.on('disconnect', () => {
    state.connected = false;
});

// Controls
socket.updateSocketJoystick = throttle(250, data => {
    socket.emit('setControlsJoystick', data);
});

socket.updateSocketButton = throttle(250, data => {
    socket.emit('setControlsButton', data);
});

// Toggle
socket.updateSocketToggle = throttle(250, (key, data) => {
    socket.emit('setToggleButton', {key, data});
});

// Gimbal
socket.updateSocketGimbal = throttle(250, data => {
    socket.emit('setGimbalPosition', data);
});
