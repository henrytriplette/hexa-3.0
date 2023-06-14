<script setup>
    import { RouterLink } from 'vue-router';
</script>

<template>
    <div class="header">
        <div class="uk-container">
            <nav id="navbar" data-uk-navbar="mode: click;" class="uk-navbar">
                <div class="uk-navbar-left nav-overlay">
                    <ul class="uk-navbar-nav">
                        <li>
                            <RouterLink to="/">Home</RouterLink>
                        </li>
                    </ul>
                </div>
                <div class="uk-navbar-center nav-overlay">
                    <RouterLink to="/" class="uk-navbar-item hera-logo" title="Hexa 3.0">Hexa 3.0</RouterLink>
                </div>
                <div class="uk-navbar-right nav-overlay">
                    <ul class="uk-navbar-nav">
                        <li>
                            <RouterLink to="/help">Help</RouterLink>
                        </li>
                        <li>
                            <RouterLink to="/about">About</RouterLink>
                        </li>
                    </ul>
                </div>
            </nav>
        </div>
    </div>
</template>

<style scoped></style>
