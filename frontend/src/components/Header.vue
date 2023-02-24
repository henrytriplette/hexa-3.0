<script setup>
    import { RouterLink } from 'vue-router';
</script>

<template>
    <div class="header">
        <nav>
            <RouterLink to="/">Home</RouterLink> |
            <RouterLink to="/about">About</RouterLink>
        </nav>
    </div>
</template>

<style scoped></style>
