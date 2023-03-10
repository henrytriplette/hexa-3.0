<template>
    <div id="hera">
        <Header />
        <RouterView />
        <Controller />
        <Footer />
    </div>
</template>

<style></style>

<script>
    import { version } from '../package.json';
    import { RouterView } from 'vue-router';

    // Head Info
    import { useHead } from '@vueuse/head';

    import Header from '@/components/Header.vue';
    import Footer from '@/components/Footer.vue';
    import Controller from '@/components/Controller.vue';

    export default {
        components: {
            Header,
            Footer,
            Controller,
        },
        setup() {
            useHead({
                title: `Ver: ${version}`,
                meta: [
                    {
                        name: 'description',
                        content: 'Page description',
                    },
                ],
            });
        },
        mounted() {
            this.$soketio.emit('connection', { data: 'Client connected!' });
        }
    };
</script>
