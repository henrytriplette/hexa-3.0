<template>
    <div id="hera">
        <Header />
        <RouterView />
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

    export default {
        components: {
            Header,
            Footer,
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
        }
    };
</script>
