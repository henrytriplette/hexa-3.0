<template>
    <div ref="status" class="controller-container uk-flex uk-flex-center uk-flex-middle">
        <div>{{ status }}</div>
    </div>
</template>

<style scoped></style>

<script>
    import 'gamecontroller.js';

    export default {
        data() {
            return {
                controller: {},
                status: 'No controller',
            };
        },
        setup() {
            window.gameControl.on('connect', () => {
                this.status = 'Gamepad connected!';
                this.$ref.status.addClass('connected');
            });

            window.gameControl.on('disconnect', () => {
                this.status = 'Gamepad disconnected!';
                this.$ref.status.removeClass('connected');
            });
        },
    };
</script>
