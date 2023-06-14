<template>
    <div class="center-panel" id="center-panel">
        <div class="uk-width-1-1">
            <ul class="uk-switcher head-switcher">
                <li class="uk-height-medium">
                    <span class="title">Camera</span>
                </li>
                <li class="uk-height-medium">
                    <div class="uk-button-group uk-width-1-1">
                        <a
                            class="uk-button uk-button-custom uk-button-small uk-width-1-2"
                            @click="updateToggle('toggle_bec_sx')"
                            >Bec SX ON</a
                        >
                        <a
                            class="uk-button uk-button-custom uk-button-small uk-width-1-2"
                            @click="updateToggle('toggle_bec_dx')"
                            >Bec DX ON</a
                        >
                    </div>
                    <div class="uk-button-group uk-width-1-1">
                        <a
                            class="uk-button uk-button-custom uk-button-small uk-width-1-2"
                            @click="updateToggle('toggle_light')"
                            >Lights ON</a
                        >
                        <a
                            class="uk-button uk-button-custom uk-button-small uk-width-1-2"
                            @click="updateToggle('toggle_gimbal')"
                            >Gimbal ON</a
                        >
                    </div>
                </li>
                <li class="uk-height-medium">
                    <div class="uk-button-group uk-width-1-1">
                        <a
                            class="uk-button uk-button-custom uk-button-small uk-width-1-1"
                            @click="updateButton('switch_gait')"
                            >Switch Gaits</a
                        >
                        <a
                            class="uk-button uk-button-custom uk-button-small uk-width-1-1"
                            @click="updateButton('adjust_leg_position')"
                            >Adjust leg position</a
                        >
                        <a
                            class="uk-button uk-button-custom uk-button-small uk-width-1-1"
                            @click="updateButton('bot_on_off')"
                            >Bot ON/OFF</a
                        >
                    </div>
                </li>
                <li class="uk-height-medium">
                    <div class="uk-button-group uk-width-1-1 uk-margin-small-bottom">
                        <a
                            class="uk-button uk-button-custom uk-button-small uk-width-1-1"
                            @click="updateGimbalReset"
                        >
                            Reset Gimbal
                        </a>
                    </div>
                    Gimbal Correction
                    <div class="uk-padding-small">
                        <label class="uk-form-label">
                            <span class="uk-text-small"
                                >X <small>({{ gimbal.x }})</small></span
                            >
                        </label>
                        <div class="uk-form-controls">
                            <input
                                v-model="gimbal.x"
                                @change="updateGimbal('x', gimbal.x)"
                                name="gimbal_x"
                                class="uk-range"
                                type="range"
                                :min="GIMBAL.minX"
                                :max="GIMBAL.maxX"
                                step="1"
                            />
                        </div>
                    </div>
                    <div class="uk-padding-small">
                        <label class="uk-form-label">
                            <span class="uk-text-small"
                                >Y <small>({{ gimbal.y }})</small></span
                            >
                        </label>
                        <div class="uk-form-controls">
                            <input
                                v-model="gimbal.y"
                                @change="updateGimbal('y', gimbal.y)"
                                name="gimbal_y"
                                class="uk-range"
                                type="range"
                                :min="GIMBAL.minY"
                                :max="GIMBAL.maxY"
                                step="1"
                            />
                        </div>
                    </div>
                    <div class="uk-padding-small">
                        <label class="uk-form-label">
                            <span class="uk-text-small"
                                >Z <small>({{ gimbal.z }})</small></span
                            >
                        </label>
                        <div class="uk-form-controls">
                            <input
                                v-model="gimbal.z"
                                @change="updateGimbal('z', gimbal.z)"
                                name="gimbal_z"
                                class="uk-range"
                                type="range"
                                :min="GIMBAL.minZ"
                                :max="GIMBAL.maxZ"
                                step="1"
                            />
                        </div>
                    </div>
                </li>
            </ul>

            <ul class="uk-flex uk-flex-center uk-tab" uk-switcher=".head-switcher">
                <li>
                    <a href="#" uk-tooltip="title: Camera"
                        ><svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="32"
                            height="32"
                            viewBox="0 0 32 32"
                        >
                            <path
                                fill="currentColor"
                                d="M12 23a6 6 0 1 1 6-6a6 6 0 0 1-6 6Zm0-10a4 4 0 1 0 4 4a4 4 0 0 0-4-4Z"
                            />
                            <path
                                fill="currentColor"
                                d="M29 27H3a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1h26a1 1 0 0 1 1 1v20a1 1 0 0 1-1 1ZM4 25h24V7H4Z"
                            />
                            <path fill="currentColor" d="M19 9h7v2h-7z" />
                            <circle cx="12" cy="17" r="1" fill="currentColor" /></svg
                    ></a>
                </li>
                <li>
                    <a href="#" uk-tooltip="title: Toggles"
                        ><svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="32"
                            height="32"
                            viewBox="0 0 15 15"
                        >
                            <g fill="none" stroke="currentColor">
                                <path d="M3.5 2.5a1 1 0 1 1 0 2a1 1 0 0 1 0-2Z" />
                                <path
                                    d="M11.5.5h-8a3 3 0 0 0 0 6h8a3 3 0 1 0 0-6Zm0 12a1 1 0 1 1 0-2a1 1 0 0 1 0 2Z"
                                />
                                <path d="M3.5 14.5h8a3 3 0 1 0 0-6h-8a3 3 0 0 0 0 6Z" />
                            </g></svg
                    ></a>
                </li>
                <li>
                    <a href="#" uk-tooltip="title: Bot"
                        ><svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="32"
                            height="32"
                            viewBox="0 0 14 14"
                        >
                            <g
                                fill="none"
                                stroke="currentColor"
                                stroke-linecap="round"
                                stroke-linejoin="round"
                            >
                                <rect width="13" height="8" x=".5" y="5.5" rx="1" />
                                <path d="M7 5.5v-5" />
                                <circle cx="10" cy="9.5" r="1.5" />
                                <circle cx="4" cy="9.5" r="1.5" />
                            </g></svg
                    ></a>
                </li>
                <li>
                    <a href="#" uk-tooltip="title: Gimbal"
                        ><svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="32"
                            height="32"
                            viewBox="0 0 24 24"
                        >
                            <path
                                fill="currentColor"
                                d="m12 2l4 4h-3v7.85l6.53 3.76L21 15.03l1.5 5.47l-5.5 1.46l1.53-2.61L12 15.58l-6.53 3.77L7 21.96L1.5 20.5L3 15.03l1.47 2.58L11 13.85V6H8l4-4Z"
                            /></svg
                    ></a>
                </li>
            </ul>
        </div>
    </div>
</template>

<style scoped>
    .center-panel {
        position: relative;
    }
</style>

<script>
    import { GIMBAL } from '@/constants/Gimbal';

    // Store
    import { storeToRefs } from 'pinia';
    import { useControlStore } from '@/store/ControlStore';

    export default {
        data() {
            return {
                ui: {},
                toggle_bec_sx: false,
                toggle_bec_dx: false,
                toggle_light: false,
                toggle_gimbal: false,
                gimbal: {
                    x: 0,
                    y: 0,
                    z: 0,
                },
            };
        },
        setup() {
            const controlStore = useControlStore();
            return {
                controlStore,
                GIMBAL,
            };
        },
        methods: {
            updateButton(key) {
                this.controlStore.updateButton(key);
            },
            updateToggle(label) {
                this.controlStore.updateToggle(label);
            },
            updateGimbal(label, value) {
                this.controlStore.updateGimbal(label, parseInt(value));
            },
            updateGimbalReset() {
                this.controlStore.updateGimbalReset();
                this.gimbal = {
                    x: 0,
                    y: 0,
                    z: 0,
                };
            },
        },
        mounted() {},
    };
</script>
