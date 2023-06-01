<template>
    <div class="center-panel" id="center-panel">
        <div class="uk-width-1-1">
            <ul class="uk-switcher head-switcher">
                <li class="uk-height-medium">Camera</li>
                <li class="uk-height-medium">
                    <a class="uk-button uk-button-primary" @click="updateToggle('toggle_bec_sx')"
                        >Bec SX ON</a
                    >
                    <a class="uk-button uk-button-primary" @click="updateToggle('toggle_bec_dx')"
                        >Bec DX ON</a
                    >
                    <a class="uk-button uk-button-primary" @click="updateToggle('toggle_light')"
                        >Lights ON</a
                    >
                    <a class="uk-button uk-button-primary" @click="updateToggle('toggle_gimbal')"
                        >Gimbal ON</a
                    >
                </li>
                <li class="uk-height-medium">
                    <a class="uk-button uk-button-primary" @click="updateButton('switch_gait')"
                        >Switch Gaits</a
                    >
                    <a
                        class="uk-button uk-button-primary"
                        @click="updateButton('adjust_leg_position')"
                        >Adjust leg position</a
                    >
                    <a class="uk-button uk-button-primary" @click="updateButton('bot_on_off')"
                        >Bot ON/OFF</a
                    >
                </li>
                <li class="uk-height-medium">
                    <button class="uk-button uk-button-primary" @click="updateGimbalReset">
                        Reset Gimbal
                    </button>
                    Gimbal Correction
                    <div class="uk-margin">
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
                    <div class="uk-margin">
                        <label class="uk-form-label">
                            <span class="uk-text-small">Y <small>({{ gimbal.y }})</small></span>
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
                    <div class="uk-margin">
                        <label class="uk-form-label">
                            <span class="uk-text-small">Z <small>({{ gimbal.z }})</small></span>
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
                <li><a href="#" uk-tooltip="title: Camera">Camera</a></li>
                <li><a href="#" uk-tooltip="title: Toggles">Toggles</a></li>
                <li><a href="#" uk-tooltip="title: Bot">Bot</a></li>
                <li><a href="#" uk-tooltip="title: Gimbal">Gimbal</a></li>
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
    // UTL.gui
    // import * as UIL from 'uil';
    import { GIMBAL } from '@/constants/Gimbal';
    import { getMaxW } from '@/utils/Utility';

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
                }
            },
        },
        mounted() {
        },
    };
</script>
