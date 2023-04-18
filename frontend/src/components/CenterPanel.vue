<template>
    <div class="center-panel" id="center-panel">
        <div id="center-gui" ref="root"></div>
    </div>
</template>

<style scoped>
    .center-panel {
        position: relative;
    }
</style>

<script>
    // UTL.gui
    import * as UIL from 'uil';
    import { GIMBAL } from '@/constants/Gimbal';

    // Store
    import { storeToRefs } from 'pinia';
    import { useControlStore } from '@/store/ControlStore';

    export default {
        data() {
            return {
                ui: {},
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
            updateToggleBot(value) {
                this.controlStore.updateToggle('bot_on_off', value);
            },
            updateToggleBecSx(value) {
                this.controlStore.updateToggle('toggle_bec_sx', value);
            },
            updateTogglBecDx(value) {
                this.controlStore.updateToggle('toggle_bec_dx', value);
            },
            updateToggleLight(value) {
                this.controlStore.updateToggle('toggle_light', value);
            },
            updateToggleGimbal(value) {
                this.controlStore.updateToggle('toggle_gimbal', value);
            },
            updateGimbalX(value) {
                this.controlStore.updateGimbal('x', value);
            },
            updateGimbalY(value) {
                this.controlStore.updateGimbal('y', value);
            },
            updateGimbalZ(value) {
                this.controlStore.updateGimbal('z', value);
            },
            updateGimbalReset(value) {
                this.controlStore.updateGimbalReset(value);
            },
            generateUI() {
                this.maxW = Math.floor(window.innerWidth / 3 - 1);

                this.ui = new UIL.Gui({
                    css: 'top:0; left:50%;',
                    center: true,
                    w: this.maxW,
                    target: this.$refs.root,
                });

                this.ui.add('title', { name: 'Center' });
                this.ui
                    .add('button', {
                        name: 'Switch Gaits',
                        value: 'switch_gait',
                    })
                    .onChange(this.updateButton);
                this.ui
                    .add('button', {
                        name: 'Adjust leg position',
                        value: 'adjust_leg_position',
                    })
                    .onChange(this.updateButton);
                this.ui.add('empty', { h: 5 });
                this.ui
                    .add('bool', {
                        name: 'Bot OFF',
                        onName: 'Bot ON',
                        mode: 1,
                        value: true,
                    })
                    .onChange(this.updateToggleBot);
                this.ui.add('empty', { h: 5 });

                this.ui
                    .add('bool', {
                        name: 'Bec SX OFF',
                        onName: 'Bec SX ON',
                        mode: 1,
                        value: false,
                    })
                    .onChange(this.updateToggleBecSx);
                this.ui
                    .add('bool', {
                        name: 'Bec DX OFF',
                        onName: 'Bec DX ON',
                        mode: 1,
                        value: false,
                    })
                    .onChange(this.updateTogglBecDx);
                this.ui
                    .add('bool', {
                        name: 'Lights OFF',
                        onName: 'Lights ON',
                        mode: 1,
                        value: false,
                    })
                    .onChange(this.updateToggleLight);
                this.ui
                    .add('bool', {
                        name: 'Gimbal OFF',
                        onName: 'Gimbal ON',
                        mode: 1,
                        value: false,
                    })
                    .onChange(this.updateToggleGimbal);

                this.ui.add('empty', { h: 5 });

                this.ui
                    .add('button', {
                        name: 'Reset Gimbal',
                        value: 'reset_gimbal',
                    })
                    .onChange(this.updateGimbalReset);

                const gimbalGroup = this.ui.add('group', {
                    name: 'Gimbal Correction',
                    color: '#E2001C',
                    h: 30,
                });
                gimbalGroup
                    .add('knob', {
                        name: 'X',
                        w: 64,
                        min: GIMBAL.minX,
                        max: GIMBAL.maxX,
                        value: 0,
                        precision: 0,
                        step: 1,
                        color: '#E2001C',
                        mode: 1,
                    })
                    .onChange(this.updateGimbalX);
                gimbalGroup
                    .add('knob', {
                        type: 'knob',
                        name: 'Y',
                        w: 64,
                        min: GIMBAL.minY,
                        max: GIMBAL.maxY,
                        value: 0,
                        precision: 0,
                        step: 1,
                        color: '#E2001C',
                        mode: 1,
                    })
                    .onChange(this.updateGimbalY);
                gimbalGroup
                    .add('knob', {
                        type: 'knob',
                        name: 'Z',
                        w: 64,
                        min: GIMBAL.minZ,
                        max: GIMBAL.maxZ,
                        value: 0,
                        precision: 0,
                        step: 1,
                        color: '#E2001C',
                        mode: 1,
                    })
                    .onChange(this.updateGimbalZ);
            },
        },
        mounted() {
            this.generateUI();
        },
    };
</script>
