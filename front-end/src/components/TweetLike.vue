<template>
    <button @click="toggleLike">
        {{ liked ? 'Unlike' : 'Like' }} ({{ count }})
    </button>
</template>

<script>
export default {
    name: 'TweetLike',
    props: [ 'tweetId' ],
    data() {
        return {
            likes: []
        }
    },
    mounted() {
        this.loadLikes();
    },
    computed: {
        count() {
            return this.likes.length;
        },
        liked() {
            let match = this.likes.filter((like) => {
                return like.userId === this.loggedInUser().userId;
            })
            
            return match.length > 0;
        }
    },
    methods: {
        loadLikes() {
            this.$axios.request({
                method: 'GET',
                url: 'https://tweeterest.ml/api/tweet-likes',
                params: {
                    tweetId: this.tweetId
                }
            })
            .then((response) => {
                this.likes = response.data;
            })
        },
        toggleLike() {
            // if already liked
            if (this.liked) {
                this.$axios.request({
                    method: 'DELETE',
                    url: 'https://tweeterest.ml/api/tweet-likes',
                    data: {
                        loginToken: this.loginToken(),
                        tweetId: this.tweetId
                    }
                })
                .then(() => {
                    this.loadLikes();
                })
            }
            // if not already liked
            else {
                this.$axios.request({
                    method: 'POST',
                    url: 'https://tweeterest.ml/api/tweet-likes',
                    data: {
                        loginToken: this.loginToken(),
                        tweetId: this.tweetId
                    }
                })
                .then(() => {
                    this.loadLikes();
                })
            }
        }
    }
}
</script>

<style lang="scss" scoped>

</style>