import { defineStore } from 'pinia';
import { socket } from '@/socket';
import { convertRange } from '@/utils/Utility';

// Const
import { JOYSTICK } from '@/constants/Joystick';
import { BUTTONS } from '@/constants/Buttons';
import { TOGGLE } from '@/constants/Toggle';

export const useControlStore = defineStore('ControlStore', {
    state: () => {
        return {
            buttons: {
                shift_mode: false,
                rotate_mode: false,
                body_up: false,
                body_down: false,
                walk_speed_up: false,
                walk_speed_down: false,
                switch_gait: false,
                adjust_leg_position: false,
                bot_on_off: false,
                double_speed: false,
                double_gait: false,
                walk_pos: false,
                single_leg: false,
                balance_mode: false,
                body_35mm: false,
            },
            toggle: {
                toggle_lights: false,
                toggle_laser: false,
            },
            joystick: {
                left_joystick: {
                    x: 128,
                    y: 128,
                },
                right_joystick: {
                    x: 128,
                    y: 128,
                },
            },
            gimbal: {
                x: 0,
                y: 0,
                z: 0,
            },
        };
    },
    actions: {
        updateJoystick(side, value) {
            this.joystick[side].x = convertRange(value[0], [-1, 1], [JOYSTICK.min, JOYSTICK.max]);
            this.joystick[side].y = convertRange(value[1], [-1, 1], [JOYSTICK.min, JOYSTICK.max]);

            socket.updateSocketJoystick(this.joystick);
        },
        updateButton(key) {
            this.buttons[key] = !this.buttons[key];

            if (BUTTONS[key]) socket.updateSocketButton(BUTTONS[key]);
        },
        updateToggle(key, value) {
            this.toggle[key] = value;
            if (TOGGLE[key]) socket.updateSocketToggle( TOGGLE[key], value );
        },
        updateGimbal(axis, value) {
            this.gimbal[axis] = value;
            socket.updateSocketGimbal(this.gimbal);
        },
    },

    // getters
    getters: {},
});
