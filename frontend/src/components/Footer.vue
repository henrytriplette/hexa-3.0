<template>
    <div class="footer uk-grid uk-child-width-1-2 uk-child-width-expand@m">
        <Connection />
        <Controller />
    </div>
</template>

<style scoped></style>

<script>
    import Connection from '@/components/Connection.vue';
    import Controller from '@/components/Controller.vue';

    export default {
        name: 'Footer',
        components: {
            Connection,
            Controller,
        },
    };
</script>
