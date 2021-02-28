<template>
    <div id="app">
        <div id="nav">
            <router-link to="/">Feed</router-link> | 
            <router-link to="/profile">Profile</router-link> | 
            <router-link to="/discover">Discover</router-link> | 
            <a v-if="loggedInUser()" href="#" @click="logout">Logout</a>
        </div>
        <router-view :key="$route.path" />
    </div>
</template>

<script>
    export default {
        methods: {
            logout() {
                this.$cookies.remove('user');
                this.$router.push({ name: 'Auth' })
            }
        }
    }
</script>

<style lang="scss">
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
}

#nav {
    padding: 30px;

    a {
        font-weight: bold;
        color: #2c3e50;

        &.router-link-exact-active {
            color: #42b983;
        }
    }
}
</style>
