<template>
    <div id="app">
        <router-view/>
    </div>
</template>

<style>
    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
    }

    html, body, #app {
        height: 100%;
    }

    html {
        width: 100%;
        min-width: 810px;
        height: 100%;
        min-height: 600px;
    }
</style>
