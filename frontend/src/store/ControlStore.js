import { defineStore } from 'pinia';

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
                toggle_lights: false,
                toggle_laser: false,
                double_speed: false,
                double_gait: false,
                walk_pos: false,
                single_leg: false,
                balance_mode: false,
            },
            joystick: {
                left_joystick: [0, 0],
                right_joystick: [0, 0],
            },
            gimbal: {
                x: 0,
                y: 0,
                z: 0,
            },
        };
    },
    actions: {
    },

    // getters
    getters: {
    },
});
