<template>
    <div class="left-panel" id="left-panel">
        <a class="uk-width-1-1 uk-margin-small" type="button" uk-toggle="target: #toggle-left">
            <span class="uk-label">Left</span>
        </a>
        <div id="toggle-left">
            <div class="uk-padding-small">
                <a
                    class="uk-button uk-button-custom uk-width-1-1 uk-button-small"
                    @click="updateButton('shift_mode')"
                    >Shift mode</a
                >
                <a
                    class="uk-button uk-button-custom uk-width-1-1 uk-button-small"
                    @click="updateButton('rotate_mode')"
                    >Rotate Mode</a
                >
            </div>
            <div class="buttons-parent uk-padding-small">
                <div class="button2">
                    <a
                        class="uk-button uk-button-none uk-button-small"
                        @click="updateButton('body_up')"
                        uk-tooltip="Body up"
                    ><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="M11 16h2v-4.2l1.6 1.6L16 12l-4-4l-4 4l1.4 1.4l1.6-1.6V16Zm1 6q-2.075 0-3.9-.788t-3.175-2.137q-1.35-1.35-2.137-3.175T2 12q0-2.075.788-3.9t2.137-3.175q1.35-1.35 3.175-2.137T12 2q2.075 0 3.9.788t3.175 2.137q1.35 1.35 2.138 3.175T22 12q0 2.075-.788 3.9t-2.137 3.175q-1.35 1.35-3.175 2.138T12 22Zm0-2q3.35 0 5.675-2.325T20 12q0-3.35-2.325-5.675T12 4Q8.65 4 6.325 6.325T4 12q0 3.35 2.325 5.675T12 20Zm0-8Z"/></svg></a>
                </div>
                <div class="button4">
                    <a
                        class="uk-button uk-button-none uk-button-small"
                        @click="updateButton('walk_speed_down')"
                        uk-tooltip="Walk speed down"
                    ><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="m12 16l1.4-1.4l-1.6-1.6H16v-2h-4.2l1.6-1.6L12 8l-4 4l4 4Zm0 6q-2.075 0-3.9-.788t-3.175-2.137q-1.35-1.35-2.137-3.175T2 12q0-2.075.788-3.9t2.137-3.175q1.35-1.35 3.175-2.137T12 2q2.075 0 3.9.788t3.175 2.137q1.35 1.35 2.138 3.175T22 12q0 2.075-.788 3.9t-2.137 3.175q-1.35 1.35-3.175 2.138T12 22Zm0-2q3.35 0 5.675-2.325T20 12q0-3.35-2.325-5.675T12 4Q8.65 4 6.325 6.325T4 12q0 3.35 2.325 5.675T12 20Zm0-8Z"/></svg></a>
                </div>
                <div class="button5"></div>
                <div class="button6">
                    <a
                        class="uk-button uk-button-none uk-button-small"
                        @click="updateButton('walk_speed_up')"
                        uk-tooltip="Walk speed up"
                    ><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="m12 16l4-4l-4-4l-1.4 1.4l1.6 1.6H8v2h4.2l-1.6 1.6L12 16Zm0 6q-2.075 0-3.9-.788t-3.175-2.137q-1.35-1.35-2.137-3.175T2 12q0-2.075.788-3.9t2.137-3.175q1.35-1.35 3.175-2.137T12 2q2.075 0 3.9.788t3.175 2.137q1.35 1.35 2.138 3.175T22 12q0 2.075-.788 3.9t-2.137 3.175q-1.35 1.35-3.175 2.138T12 22Zm0-2q3.35 0 5.675-2.325T20 12q0-3.35-2.325-5.675T12 4Q8.65 4 6.325 6.325T4 12q0 3.35 2.325 5.675T12 20Zm0-8Z"/></svg></a>
                </div>
                <div class="button8">
                    <a
                        class="uk-button uk-button-none uk-button-small"
                        @click="updateButton('body_down')"
                        uk-tooltip="Body Down"
                    ><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="m12 16l4-4l-1.4-1.4l-1.6 1.6V8h-2v4.2l-1.6-1.6L8 12l4 4Zm0 6q-2.075 0-3.9-.788t-3.175-2.137q-1.35-1.35-2.137-3.175T2 12q0-2.075.788-3.9t2.137-3.175q1.35-1.35 3.175-2.137T12 2q2.075 0 3.9.788t3.175 2.137q1.35 1.35 2.138 3.175T22 12q0 2.075-.788 3.9t-2.137 3.175q-1.35 1.35-3.175 2.138T12 22Zm0-2q3.35 0 5.675-2.325T20 12q0-3.35-2.325-5.675T12 4Q8.65 4 6.325 6.325T4 12q0 3.35 2.325 5.675T12 20Zm0-8Z"/></svg></a>
                </div>
            </div>
        </div>

        <div
            id="left-joystick"
            ref="leftJoystick"
            class="uk-height-medium uk-position-relative"
        ></div>
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
