<template>
    <div ref="connection" class="connection-container  uk-flex uk-flex-center uk-flex-middle" :class="{ connected: connected }">
        <div>{{ connected ? 'Server connected' : 'Server disconnected' }}</div>
    </div>
</template>

<style scoped></style>

<script>
    import { state } from '@/socket';

    export default {
        data() {
            return {};
        },
        computed: {
            connected() {
                return state.connected;
            },
        },
    };
</script>
