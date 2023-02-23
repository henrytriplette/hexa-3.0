<template>
    <div class="container">
        <div class="header"></div>
        <div id="left"></div>
        <div id="center"></div>
        <div id="right"></div>
        <div class="footer"></div>
    </div>
</template>

<style scoped></style>

<script>
    import { version } from '../package.json';

    // Socket IO
    import { io } from 'socket.io-client';

    // UTL.gui
    import * as UIL from 'uil';

    // Head Info
    import { useHead } from '@vueuse/head';

    export default {
        setup() {
            const socket = io('localhost:5000');

            window.onbeforeunload = () => {
                this.socket.emit('disconnect');
            };

            useHead({
                title: `Ver: ${version}`,
                meta: [
                    {
                        name: 'description',
                        content: 'Page description',
                    },
                ],
            });
            const ui = {
                left: null,
                center: null,
                right: null,
            };

            const data = {
                shift_mode: false,
                rotate_mode: false,
                body_up: 50,
                walk_speed: 50,
                switch_gait: false,
                adjust_leg_position: false,
                bot_on_off: false,
                toggle_lights: false,
                toggle_laser: false,
                double_speed: false,
                double_gait: false,
                walk_pos: false,
                single_leg: false,
                balance_mode: false,
            };

            const joystick = {
                left_joystick: [0, 0],
                right_joystick: [0, 0],
            };

            const gimbal = {
                x: 0,
                y: 0,
                z: 0,
            };

            return {
                socket,
                ui,
                data,
                joystick,
                gimbal,
            };
        },
        methods: {
            updateButton(value, key) {
                !this.data[key];
                console.log(value, this.data);
            },
            updateJoystick(value, key) {
                this.joystick[key] = value;
                console.log(this.joystick);
            },
            updateGimbal(value, key) {
                this.gimbal[key] = value;
                console.log(this.gimbal);
            },
            onWindowResize() {
                let w = window.innerWidth / 3;
                for (const ui in this.ui) {
                    this.ui[ui].setWidth(Math.floor(w));
                }
            },
            generateUI() {
                this.maxW = Math.floor(window.innerWidth / 3 - 1);

                this.ui.left = new UIL.Gui({
                    css: 'top:0; left:50%;',
                    center: true,
                    w: this.maxW,
                    target: document.querySelector('#left'),
                }); // .onChange(this.updateValues);

                this.ui.center = new UIL.Gui({
                    css: 'top:0; left:50%;',
                    center: true,
                    w: this.maxW,
                    target: document.querySelector('#center'),
                }); // .onChange(this.updateValues);

                this.ui.right = new UIL.Gui({
                    css: 'top:0; left:50%;',
                    center: true,
                    w: this.maxW,
                    target: document.querySelector('#right'),
                }); // .onChange(this.updateValues);

                this.ui.left.add('title', { name: 'Left' });
                this.ui.left
                    .add(this.data, 'shift_mode', {
                        type: 'button',
                        name: 'Shift mode',
                        value: 'shift_mode',
                        w: 50,
                    })
                    .onChange(this.updateButton);
                this.ui.left
                    .add(this.data, 'rotate_mode', {
                        type: 'button',
                        name: 'Rotate Mode',
                        value: 'rotate_mode',
                        w: 50,
                    })
                    .onChange(this.updateButton);
                this.ui.left.add('empty', { h: 5 });
                this.ui.left
                    .add(this.data, 'body_up', {
                        rename: 'Body Position',
                        type: 'slide',
                        min: 0,
                        max: 100,
                        precision: 1,
                        step: 1,
                    })
                    .onChange(this.updateValues);
                this.ui.left
                    .add(this.data, 'walk_speed', {
                        rename: 'Walk Speed',
                        type: 'slide',
                        min: 0,
                        max: 100,
                        precision: 1,
                        step: 1,
                    })
                    .onChange(this.updateValues);
                this.ui.left
                    .add(this.joystick, 'left_joystick', {
                        type: 'joystick',
                        rename: 'Move',
                        multiplicator: 1,
                        precision: 2,
                        color: '#E2001C',
                    })
                    .onChange(this.updateJoystick);

                this.ui.center.add('title', { name: 'Center' });
                this.ui.center
                    .add(this.data, 'switch_gait', {
                        type: 'button',
                        name: 'Switch Gaits',
                        value: 'switch_gait',
                    })
                    .onChange(this.updateButton);
                this.ui.center
                    .add(this.data, 'adjust_leg_position', {
                        type: 'button',
                        name: 'Adjust leg position',
                        value: 'adjust_leg_position',
                    })
                    .onChange(this.updateButton);
                this.ui.center
                    .add(this.data, 'bot_on_off', {
                        rename: 'Bot OFF',
                        onName: 'Bot ON',
                        value: 'bot_on_off',
                        mode: 1,
                    })
                    .onChange(this.updateButton);
                this.ui.center.add('empty', { h: 5 });
                this.ui.center
                    .add(this.data, 'toggle_lights', {
                        rename: 'Lights OFF',
                        onName: 'Lights ON',
                        value: 'toggle_lights',
                        mode: 1,
                    })
                    .onChange(this.updateButton);
                this.ui.center
                    .add(this.data, 'toggle_laser', {
                        rename: 'Laser OFF',
                        onName: 'Laser ON',
                        value: 'toggle_laser',
                        mode: 1,
                    })
                    .onChange(this.updateButton);
                this.ui.center.add('empty', { h: 5 });

                const gimbalGroup = this.ui.center.add('group', {
                    name: 'Gimbal Correction',
                    color: '#E2001C',
                    h: 30,
                });
                gimbalGroup
                    .add(this.gimbal, 'x', {
                        type: 'knob',
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
                    .onChange(this.updateGimbal);
                gimbalGroup
                    .add(this.gimbal, 'y', {
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
                    .onChange(this.updateGimbal);
                gimbalGroup
                    .add(this.gimbal, 'z', {
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
                    .onChange(this.updateGimbal);

                this.ui.right.add('title', { name: 'Right' });
                this.ui.right
                    .add(this.data, 'double_speed', {
                        type: 'button',
                        name: 'Double Speed',
                        value: 'double_speed',
                    })
                    .onChange(this.updateButton);
                this.ui.right
                    .add(this.data, 'double_gait', {
                        type: 'button',
                        name: 'Double Gait',
                        value: 'double_gait',
                    })
                    .onChange(this.updateButton);
                this.ui.right.add('empty', { h: 5 });

                this.ui.right
                    .add(this.data, 'walk_pos', {
                        type: 'button',
                        name: 'Walk Pos',
                        value: 'walk_pos',
                    })
                    .onChange(this.updateButton);
                this.ui.right
                    .add(this.data, 'single_leg', {
                        type: 'button',
                        name: 'Single Leg',
                        value: 'single_leg',
                    })
                    .onChange(this.updateButton);
                this.ui.right
                    .add(this.data, 'balance_mode', {
                        type: 'button',
                        name: 'Balance mode',
                        value: 'balance_mode',
                    })
                    .onChange(this.updateButton);
                this.ui.right
                    .add(this.joystick, 'right_joystick', {
                        type: 'joystick',
                        rename: 'Rotate',
                        multiplicator: 1,
                        precision: 2,
                        color: '#E2001C',
                    })
                    .onChange(this.updateJoystick);
            },
        },
        created() {
            window.addEventListener('resize', this.onWindowResize, false);
        },
        destroyed() {
            window.removeEventListener('resize', this.onWindowResize, false);
        },
        mounted() {
            console.log('Ver:', version);
            this.socket.emit('connection', { data: 'Client connected!' });
            this.generateUI();
        },
    };
</script>
