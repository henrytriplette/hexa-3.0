<template>
    <div class="left-panel" id="left-panel">
        <div id="left-gui" ref="root"></div>
    </div>
</template>

<style scoped>
    .left-panel {
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
                this.controlStore.updateButton(key);
            },
            updateJoystick(value) {
                this.controlStore.updateJoystick('left_joystick', value);
            },
            generateUI() {
                this.maxW = Math.floor(window.innerWidth / 3 - 1);

                this.ui = new UIL.Gui({
                    css: 'top:0; left:50%;',
                    center: true,
                    w: this.maxW,
                    target: this.$refs.root,
                });

                this.ui.add('title', { name: 'Left' });
                this.ui
                    .add('button', {
                        name: 'Shift mode',
                        value: 'shift_mode',
                    })
                    .onChange(this.updateButton);
                this.ui
                    .add('button', {
                        name: 'Rotate Mode',
                        value: 'rotate_mode',
                    })
                    .onChange(this.updateButton);

                this.ui.add('empty', { h: 5 });

                this.ui
                    .add('button', {
                        name: 'Body up',
                        value: 'body_up',
                    })
                    .onChange(this.updateButton);
                this.ui
                    .add('button', {
                        name: 'Body down',
                        value: 'body_down',
                    })
                    .onChange(this.updateButton);

                this.ui
                    .add('button', {
                        name: 'Walk speed up',
                        value: 'walk_speed_up',
                    })
                    .onChange(this.updateButton);
                this.ui
                    .add('button', {
                        name: 'Walk speed down',
                        value: 'walk_speed_down',
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
