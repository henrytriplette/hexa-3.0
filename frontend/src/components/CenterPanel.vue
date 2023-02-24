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
                this.controlStore.buttons[key] = !this.controlStore.buttons[key];
                console.log(key, this.controlStore.buttons[key]);
            },
            updateToggleBot(value) {
                this.controlStore.buttons.bot_on_off = value;
                console.log(this.controlStore.buttons.bot_on_off);
            },
            updateToggleLights(value) {
                this.controlStore.buttons.toggle_lights = value;
                console.log(this.controlStore.buttons.toggle_lights);
            },
            updateToggleLaser(value) {
                this.controlStore.buttons.toggle_laser = value;
                console.log(this.controlStore.buttons.toggle_laser);
            },
            updateGimbalX(value) {
                this.controlStore.gimbal.x = value;
            },
            updateGimbalY(value) {
                this.controlStore.gimbal.y = value;
            },
            updateGimbalZ(value) {
                this.controlStore.gimbal.z = value;
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
                        name: 'Lights OFF',
                        onName: 'Lights ON',
                        mode: 1,
                        value: false,
                    })
                    .onChange(this.updateToggleLights);
                this.ui
                    .add('bool', {
                        name: 'Laser OFF',
                        onName: 'Laser ON',
                        mode: 1,
                        value: false,
                    })
                    .onChange(this.updateToggleLaser);

                this.ui.add('empty', { h: 5 });

                const gimbalGroup = this.ui.add('group', {
                    name: 'Gimbal Correction',
                    color: '#E2001C',
                    h: 30,
                });
                gimbalGroup
                    .add('knob', {
                        name: 'X',
                        w: 64,
                        min: -100,
                        max: 100,
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
                        min: -100,
                        max: 100,
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
                        min: -100,
                        max: 100,
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
