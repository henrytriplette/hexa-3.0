<template>
    <div class="left-panel" id="left-panel">
        <a class="uk-width-1-1 uk-margin-small" type="button" uk-toggle="target: #toggle-left">
            <span class="uk-label">Left</span>
        </a>
        <div id="toggle-left">
            <div class="uk-padding-small">
                <a
                    class="uk-button uk-button-primary uk-width-1-1 uk-margin-small-bottom"
                    @click="updateButton('shift_mode')"
                    >Shift mode</a
                >
                <a
                    class="uk-button uk-button-primary uk-width-1-1 uk-margin-small-bottom"
                    @click="updateButton('rotate_mode')"
                    >Rotate Mode</a
                >
            </div>
            <div class="buttons-parent uk-padding-small">
                <div class="button2">
                    <a
                        class="uk-button uk-button-primary"
                        @click="updateButton('body_up')"
                        uk-icon="triangle-up"
                        uk-tooltip="Body up"
                    ></a>
                </div>
                <div class="button4">
                    <a
                        class="uk-button uk-button-primary"
                        @click="updateButton('walk_speed_down')"
                        uk-icon="triangle-left"
                        uk-tooltip="Walk speed down"
                    ></a>
                </div>
                <div class="button5"></div>
                <div class="button6">
                    <a
                        class="uk-button uk-button-primary"
                        @click="updateButton('walk_speed_up')"
                        uk-icon="triangle-right"
                        uk-tooltip="Walk speed up"
                    ></a>
                </div>
                <div class="button8">
                    <a
                        class="uk-button uk-button-primary"
                        @click="updateButton('body_down')"
                        uk-icon="triangle-down"
                        uk-tooltip="Body Down"
                    ></a>
                </div>
            </div>
        </div>

        <div id="left-joystick" ref="leftJoystick"></div>
        <div class="left-joystick-values">
            {{ leftJoystickValue[0] }}, {{ leftJoystickValue[1] }}
        </div>
    </div>
</template>

<style scoped>
    #left-joystick {
        position: relative;
    }
</style>

<script>
    // Store
    import { storeToRefs } from 'pinia';
    import { useControlStore } from '@/store/ControlStore';

    import Nipple from 'nipplejs';
    import { getMaxW } from '@/utils/Utility';

    export default {
        data() {
            return {
                leftJoystickValue: [0, 0],
            };
        },
        setup() {
            const controlStore = useControlStore();
            return {
                controlStore,
            };
        },
        methods: {
            updateButton(key) {
                this.controlStore.updateButton(key);
            },
            updateJoystick(value) {
                this.controlStore.updateJoystick('left_joystick', value);
            },
        },
        mounted() {
            const manager = Nipple.create({
                zone: this.$refs.leftJoystick,
                mode: 'static',
                position: { left: '50%', top: '50%' },
                size: getMaxW() * 0.75,
                catchDistance: 150,
                color: 'white',
                restJoystick: true,
            });

            // Handle NippleJS events or actions
            manager.on('start', (event, data, parent) => {
                this.leftJoystickValue = [0, 0];
                this.updateJoystick(this.leftJoystickValue);
            });

            manager.on('move', (event, data, parent) => {
                this.leftJoystickValue = [
                    parseFloat(data.vector.x.toFixed(2)),
                    parseFloat(data.vector.y.toFixed(2)),
                ];
                this.updateJoystick(this.leftJoystickValue);
            });

            manager.on('end', (event, data, parent) => {
                this.leftJoystickValue = [0, 0];
                this.updateJoystick(this.leftJoystickValue);
            });

            // Access the NippleJS instance if needed
            this.nipple = manager.get(0);
        },
    };
</script>
