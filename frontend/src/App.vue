<template>
    <div></div>
</template>

<style scoped></style>

<script>
    import { version } from '../package.json';

    // Socket IO
    import { io } from 'socket.io-client';

    // Analytics Tracking
    import { useHead } from '@vueuse/head';

    export default {
        setup() {
            const socket = io('localhost:5000');

            useHead({
                title: `Ver: ${version}`,
                meta: [
                    {
                        name: 'description',
                        content: 'Page description',
                    },
                ],
            });

            return {
                socket,
            };
        },
        mounted() {
            console.log('Ver:', version);
            
            this.socket.emit('connection', {data: 'Client connected!'});
        },
    };
</script>
