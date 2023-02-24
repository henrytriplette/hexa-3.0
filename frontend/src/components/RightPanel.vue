<template>
    <div class="right-panel" id="right-panel">
        <div id="right-gui" ref="root"></div>
    </div>
</template>

<style scoped>
    .right-panel {
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
            updateJoystick(value) {
                this.controlStore.joystick.right_joystick = value;
                console.log(this.controlStore.joystick.right_joystick);
            },
            generateUI() {
                this.maxW = Math.floor(window.innerWidth / 3 - 1);

                this.ui = new UIL.Gui({
                    css: 'top:0; left:50%;',
                    center: true,
                    w: this.maxW,
                    target: this.$refs.root,
                });

                this.ui.add('title', { name: 'Right' });
                this.ui
                    .add('button', {
                        name: 'Double Speed',
                        value: 'double_speed',
                    })
                    .onChange(this.updateButton);
                this.ui
                    .add('button', {
                        name: 'Double Gait',
                        value: 'double_gait',
                    })
                    .onChange(this.updateButton);

                this.ui.add('empty', { h: 5 });

                this.ui
                    .add('button', {
                        name: 'Walk Pos',
                        value: 'walk_pos',
                    })
                    .onChange(this.updateButton);
                this.ui
                    .add('button', {
                        name: 'Single Leg',
                        value: 'single_leg',
                    })
                    .onChange(this.updateButton);

                this.ui
                    .add('button', {
                        name: 'Balance mode',
                        value: 'balance_mode',
                    })
                    .onChange(this.updateButton);

                this.ui
                    .add('joystick', {
                        name: 'Move',
                        multiplicator: 1,
                        precision: 2,
                        color: '#E2001C',
                    })
                    .onChange(this.updateJoystick);
            },
        },
        mounted() {
            this.generateUI();
        },
    };
</script>
