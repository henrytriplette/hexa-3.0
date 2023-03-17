import { createApp } from 'vue';
import { createPinia } from 'pinia';
import { createHead } from '@vueuse/head';

import './style.sass';

import App from '@/App.vue';
import router from '@/router';

const app = createApp(App);
const head = createHead();
const pinia = createPinia();

app.use(pinia).use(router).use(head);

app.mount('#app');
