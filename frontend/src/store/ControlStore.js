import { defineStore } from 'pinia';
import { socket } from '@/socket';
import { convertRange } from '@/utils/Utility';

// Const
import { JOYSTICK } from '@/constants/Joystick';
import { BUTTONS } from '@/constants/Buttons';
import { TOGGLE } from '@/constants/Toggle';
import { GIMBAL } from '@/constants/Gimbal';

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
                toggle_bec_sx: false,
                toggle_bec_dx: false,
                toggle_light: false,
                toggle_gimbal: false,
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
                reset_gimbal: false,
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
        updateToggle(key) {
            this.toggle[key] = !this.toggle[key];
            if (TOGGLE[key]) socket.updateSocketToggle(TOGGLE[key], this.toggle[key]);
        },
        updateGimbal(axis, value) {
            this.gimbal[axis] = value;
            socket.updateSocketGimbal(this.gimbal);
        },
        updateGimbalReset() {
            this.gimbal = {
                x: 0,
                y: 0,
                z: 0,
                reset_gimbal: false,
            };

            socket.updateSocketGimbalReset(GIMBAL.gimbal_reset, this.gimbal.reset_gimbal);
        },
    },

    // getters
    getters: {},
});
