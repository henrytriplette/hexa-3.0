<template>
    <div class="right-panel" id="right-panel">
        <a class="uk-width-1-1 uk-margin-small" type="button" uk-toggle="target: #toggle-right">
            <span class="uk-label">Right</span>
        </a>
        <div id="toggle-right">
            <div class="uk-padding-small">
                <a
                    class="uk-button uk-button-primary uk-width-1-1 uk-margin-small-bottom"
                    @click="updateButton('double_speed')"
                    >Double Speed</a
                >
                <a
                    class="uk-button uk-button-primary uk-width-1-1 uk-margin-small-bottom"
                    @click="updateButton('double_gait')"
                    >Double Gait</a
                >
            </div>
            <div class="buttons-parent uk-padding-small">
                <div class="button2">
                    <a
                        class="uk-button uk-button-primary"
                        @click="updateButton('walk_pos')"
                        uk-tooltip="Walk Pos"
                        uk-icon="triangle-up"
                    ></a>
                </div>
                <div class="button4">
                    <a
                        class="uk-button uk-button-primary"
                        @click="updateButton('single_leg')"
                        uk-tooltip="Single Leg"
                        uk-icon="triangle-up"
                    ></a>
                </div>
                <div class="button6">
                    <a
                        class="uk-button uk-button-primary"
                        @click="updateButton('balance_mode')"
                        uk-tooltip="Balance mode"
                        uk-icon="triangle-up"
                    ></a>
                </div>
                <div class="button8">
                    <a
                        class="uk-button uk-button-primary"
                        @click="updateButton('body_35mm')"
                        uk-tooltip="Body 35mm mode"
                        uk-icon="triangle-up"
                    ></a>
                </div>
            </div>
        </div>
        <div id="right-joystick" ref="rightJoystick"></div>
        <div class="right-joystick-values">
            {{ rightJoystickValue[0] }}, {{ rightJoystickValue[1] }}
        </div>
    </div>
</template>

<style scoped>
    #right-joystick {
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
                rightJoystickValue: [0, 0],
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
                this.controlStore.updateJoystick('right_joystick', value);
            },
        },
        mounted() {
            const manager = Nipple.create({
                zone: this.$refs.rightJoystick,
                mode: 'static',
                position: { left: '50%', top: '50%' },
                size: getMaxW() * 0.75,
                catchDistance: 150,
                color: 'white',
                restJoystick: true,
            });

            // Handle NippleJS events or actions
            manager.on('start', (event, data, parent) => {
                this.rightJoystickValue = [0, 0];
                this.updateJoystick(this.rightJoystickValue);
            });

            manager.on('move', (event, data, parent) => {
                this.rightJoystickValue = [
                    parseFloat(data.vector.x.toFixed(2)),
                    parseFloat(data.vector.y.toFixed(2)),
                ];
                this.updateJoystick(this.rightJoystickValue);
            });

            manager.on('end', (event, data, parent) => {
                this.rightJoystickValue = [0, 0];
                this.updateJoystick(this.rightJoystickValue);
            });

            // Access the NippleJS instance if needed
            this.nipple = manager.get(0);
        },
    };
</script>
