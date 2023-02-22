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
                this.ui.clear();
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
                left_joystick: [0, 0],
                switch_gait: false,
                adjust_leg_position: false,
                bot_on_off: false,
                toggle_lights: false,
                toggle_laser: false,
                gimbal: {
                    x: 0,
                    y: 0,
                    z: 0,
                },
                double_speed: false,
                double_gait: false,
                walk_pos: false,
                single_leg: false,
                balance_mode: false,
                right_joystick: [0, 0],
            };

            return {
                socket,
                ui,
                data,
            };
        },
        methods: {
            updateValues(value, key) {
                this.data[key] = value;
                console.log(this.data.right_joystick);
            },
            updateButton(key) {
                this.data[key] = !this.data[key];
                console.log(this.data);
            },
            onWindowResize() {
                let w = window.innerWidth / 3;
                for (const ui in this.ui) {
                    this.ui[ui].setWidth(Math.floor(w));
                }
            },
            generateUI() {
                this.maxW = window.innerWidth / 3;

                this.ui.left = new UIL.Gui({
                    css: 'top:0; left:50%;',
                    center: true,
                    w: this.maxW,
                    target: document.querySelector('#left'),
                }).onChange(this.updateValues);

                this.ui.center = new UIL.Gui({
                    css: 'top:0; left:50%;',
                    center: true,
                    w: this.maxW,
                    target: document.querySelector('#center'),
                }).onChange(this.updateValues);

                this.ui.right = new UIL.Gui({
                    css: 'top:0; left:50%;',
                    center: true,
                    w: this.maxW,
                    target: document.querySelector('#right'),
                }).onChange(this.updateValues);

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
                this.ui.left.add(this.data, 'body_up', {
                    rename: 'Body Position',
                    type: 'slide',
                    min: 0,
                    max: 100,
                    precision: 1,
                    step: 1,
                });
                this.ui.left.add(this.data, 'walk_speed', {
                    rename: 'Walk Speed',
                    type: 'slide',
                    min: 0,
                    max: 100,
                    precision: 1,
                    step: 1,
                });
                this.ui.left.add(this.data, 'left_joystick', {
                    type: 'joystick',
                    rename: 'Move',
                    multiplicator: 1,
                    precision: 2,
                    color: '#D4B87B',
                });

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
                        type: 'button',
                        name: 'Bot on/off',
                        value: 'bot_on_off',
                    })
                    .onChange(this.updateButton);
                this.ui.center.add('empty', { h: 5 });
                this.ui.center.add(this.data, 'toggle_lights', {
                    name: 'Lights OFF',
                    onName: 'Lights ON',
                    value: false,
                    mode: 1,
                });
                this.ui.center.add(this.data, 'toggle_laser', {
                    name: 'Laser OFF',
                    onName: 'Laser ON',
                    value: false,
                    mode: 1,
                });
                this.ui.center.add('empty', { h: 5 });

                this.gimbal = this.ui.center.add('group', {
                    name: 'Gimbal Correction',
                    color: '#D4B87B',
                    h: 30,
                });
                this.gimbal.add(this.data.gimbal, 'x', {
                    type: 'knob',
                    name: 'X',
                    w: 64,
                    min: -100,
                    max: 100,
                    value: 0,
                    precision: 0,
                    step: 1,
                    color: '#D4B87B',
                    mode: 1,
                });
                this.gimbal.add(this.data.gimbal, 'y', {
                    type: 'knob',
                    name: 'Y',
                    w: 64,
                    min: -100,
                    max: 100,
                    value: 0,
                    precision: 0,
                    step: 1,
                    color: '#D4B87B',
                    mode: 1,
                });
                this.gimbal.add(this.data.gimbal, 'z', {
                    type: 'knob',
                    name: 'Z',
                    w: 64,
                    min: -100,
                    max: 100,
                    value: 0,
                    precision: 0,
                    step: 1,
                    color: '#D4B87B',
                    mode: 1,
                });

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
                this.ui.right.add(this.data, 'right_joystick', {
                    type: 'joystick',
                    rename: 'Rotate',
                    multiplicator: 1,
                    precision: 2,
                    color: '#D4B87B',
                });
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
