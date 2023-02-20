import { createApp } from 'vue'
import { createHead } from "@vueuse/head";

import './style.sass'

import App from './App.vue'

const app = createApp(App);
const head = createHead();

app.use(head).mount("#app");

