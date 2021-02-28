<template>
    <div id="login-register">
        <section id="login">
            <h3>Login</h3>
            <form @submit.prevent="login">
                <label>Email</label>
                <input type="email" v-model="loginForm.email">
                <br>
                <label>Password</label>
                <input type="password" v-model="loginForm.password">
                <br>
                <button type="submit">Login</button>
            </form>
        </section>
        <hr>
        <section id="register">
            <h3>Register</h3>
            <form @submit.prevent="register">
                <label>Email</label>
                <input type="email" v-model="registerForm.email">
                <br>
                <label>Username</label>
                <input type="text" v-model="registerForm.username">
                <br>
                <label>Password</label>
                <input type="password" v-model="registerForm.password">
                <br>
                <label>Birthdate</label>
                <input type="date" v-model="registerForm.birthdate">
                <br>
                <label>Bio</label>
                <textarea v-model="registerForm.bio"></textarea>
                <br>
                <button type="submit">Register Account</button>
            </form>
        </section>
    </div>
</template>

<script>
export default {
    name: 'Auth',
    data() {
        return {
            loginForm: {
                email: '',
                password: ''
            },
            registerForm: {
                email: '',
                username: '',
                password: '',
                birthdate: '',
                bio: ''
            }
        }
    },
    methods: {
        login() {
            this.$axios.request({
                method: 'POST',
                url: 'https://tweeterest.ml/api/login',
                data: {
                    email: this.loginForm.email,
                    password: this.loginForm.password
                }
            })
            .then((response) => {
                if (response.status === 201) {
                    // successful path
                    this.$cookies.set('user', response.data, '1h');
                    this.$router.push({ name: 'Feed' })
                } else {
                    alert('ERROR')
                }
            });
        },
        register() {
            this.$axios.request({
                method: 'POST',
                url: 'https://tweeterest.ml/api/users',
                data: {
                    email: this.registerForm.email,
                    username: this.registerForm.username,
                    password: this.registerForm.password,
                    birthdate: this.registerForm.birthdate,
                    bio: this.registerForm.bio
                }
            }).then((response) => {              
                if (response.status === 201) {
                    // successful path
                    this.$cookies.set('user', response.data, '1h');
                    this.$router.push({ name: 'Feed' })
                } else {
                    alert('ERROR')
                }
            });
        }
    }
}
</script>

<style lang="scss" scoped>