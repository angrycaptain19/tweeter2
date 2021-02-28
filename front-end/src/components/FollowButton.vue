<template>
    <button @click="toggleFollow">
        {{ following ? 'Unfollow' : 'Follow' }}
    </button>
</template>

<script>
export default {
    name: 'FollowButton',
    props: ['userId'],
    data(){
        return {
            followers: []
        }
    },
    computed: {
        following() {
            let match = this.followers.reduce((total, follower) => {
                if (follower.id === this.loggedInUser().userId) {
                    
                    return total + 1;
                }
                return total;
            }, 0)
            return match > 0;
        }
    },
    mounted() {
        this.loadFollowers();
    },
    methods: {
        loadFollowers() {
            this.$axios.request({
                method: 'GET',
                url: 'https://tweeterest.ml/api/followers',
                params: {
                    userId: this.userId
                }
            })
            .then((response) => {
                this.followers = response.data;
            })
        },
        toggleFollow() {
            this.$axios.request({
                method: this.following ? 'DELETE' : 'POST',
                url: 'https://tweeterest.ml/api/follows',
                data: {
                    loginToken: this.loginToken(),
                    followId: this.userId
                }
            })
            .then(() => {
                this.loadFollowers();
            })
        }
    }
}
</script>
