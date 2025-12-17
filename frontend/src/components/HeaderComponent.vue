<script setup lang="ts">
import { RouterLink } from 'vue-router';


</script>

<template>
    <header>
        <div class="container">
            <RouterLink type="button" to="/" :class="{'active': $route.path === '/'}">ГЛАВНАЯ</RouterLink>
            <RouterLink type="button" to="/catalog" :class="{'active': $route.path === '/catalog'}">КАТАЛОГ</RouterLink>
            <img alt="Vue logo" class="logo" src="../assets/logo.png" />
            <RouterLink type="button" to="/reviews" :class="{'active': $route.path === '/reviews'}">ОТЗЫВЫ</RouterLink>
            <RouterLink type="button" to="/orders" :class="{'active': $route.path === '/orders'}">ЛИЧНЫЙ КАБИНЕТ</RouterLink>
        </div>
    </header>
</template>

<style scoped>
    header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 120px;
        z-index: 1000;

        display: flex;
        justify-content: center;
        background-color: rgba(0, 0, 0, 0.5); ;
    }

    .container {
        width: 1200px;
        height: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    a {
        color: white;
        font-size: 20px;
        text-decoration: none;
    }

    a:hover {
        text-decoration: underline;
    }

    .active {
        text-decoration: underline;
    }

    .logo {
        width: 200px;
        height: 100px;
    }
</style>