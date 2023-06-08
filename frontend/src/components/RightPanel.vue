<template>
    <div class="right-panel" id="right-panel">
        <a class="uk-width-1-1 uk-margin-small" type="button" uk-toggle="target: #toggle-right">
            <span class="uk-label">Right</span>
        </a>
        <div id="toggle-right">
            <div class="uk-padding-small">
                <a
                    class="uk-button uk-button-custom uk-button-small uk-width-1-1"
                    @click="updateButton('double_speed')"
                    >Double Speed</a
                >
                <a
                    class="uk-button uk-button-custom uk-button-small uk-width-1-1"
                    @click="updateButton('double_gait')"
                    >Double Gait</a
                >
            </div>
            <div class="buttons-parent uk-padding-small">
                <div class="button2">
                    <a
                        class="uk-button uk-button-none uk-button-small"
                        @click="updateButton('walk_pos')"
                        uk-tooltip="Walk Pos"
                    ><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path stroke-linecap="round" stroke-linejoin="round" d="m12 8l-4 6h8l-4-6Z"/></g></svg></a>
                </div>
                <div class="button4">
                    <a
                        class="uk-button uk-button-none uk-button-small"
                        @click="updateButton('single_leg')"
                        uk-tooltip="Single Leg"
                    ><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="M18 12c0-3.31-2.69-6-6-6s-6 2.69-6 6s2.69 6 6 6s6-2.69 6-6m-6-4a3.999 3.999 0 1 1 .002 8.002A3.999 3.999 0 0 1 12 8m8-4H4v16h16V4m2-2v20H2V2h20Z"/></svg></a>
                </div>
                <div class="button6">
                    <a
                        class="uk-button uk-button-none uk-button-small"
                        @click="updateButton('balance_mode')"
                        uk-tooltip="Balance mode"
                    ><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="M12 2C6.47 2 2 6.47 2 12s4.47 10 10 10s10-4.47 10-10S17.53 2 12 2zm0 18c-4.42 0-8-3.58-8-8s3.58-8 8-8s8 3.58 8 8s-3.58 8-8 8z"/></svg></a>
                </div>
                <div class="button8">
                    <a
                        class="uk-button uk-button-none uk-button-small"
                        @click="updateButton('body_35mm')"
                        uk-tooltip="Body 35mm mode"
                    ><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="m12 13.4l2.9 2.9q.275.275.7.275t.7-.275q.275-.275.275-.7t-.275-.7L13.4 12l2.9-2.9q.275-.275.275-.7t-.275-.7q-.275-.275-.7-.275t-.7.275L12 10.6L9.1 7.7q-.275-.275-.7-.275t-.7.275q-.275.275-.275.7t.275.7l2.9 2.9l-2.9 2.9q-.275.275-.275.7t.275.7q.275.275.7.275t.7-.275l2.9-2.9Zm0 8.6q-2.075 0-3.9-.788t-3.175-2.137q-1.35-1.35-2.137-3.175T2 12q0-2.075.788-3.9t2.137-3.175q1.35-1.35 3.175-2.137T12 2q2.075 0 3.9.788t3.175 2.137q1.35 1.35 2.138 3.175T22 12q0 2.075-.788 3.9t-2.137 3.175q-1.35 1.35-3.175 2.138T12 22Zm0-2q3.35 0 5.675-2.325T20 12q0-3.35-2.325-5.675T12 4Q8.65 4 6.325 6.325T4 12q0 3.35 2.325 5.675T12 20Zm0-8Z"/></svg></a>
                </div>
            </div>
        </div>
        <div
            id="right-joystick"
            ref="rightJoystick"
            class="uk-height-medium uk-position-relative"
        ></div>
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
