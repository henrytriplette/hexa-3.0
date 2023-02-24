import { createApp } from 'vue';
import { createPinia } from 'pinia';
import { createHead } from '@vueuse/head';
import { io } from 'socket.io-client';

import './style.sass';

import App from '@/App.vue';
import router from '@/router';

const app = createApp(App);
const head = createHead();
const pinia = createPinia();

app.config.globalProperties.$soketio = io(import.meta.env.VITE_SOCKETIO_SERVER);

app.use(pinia).use(router).use(head);

app.mount('#app');
