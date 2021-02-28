<template>
    <form class="tweet-create" @submit.prevent="postTweet">
        <h3>Write a Tweet</h3>
        <textarea v-model="content" placeholder="What's on your mind?"></textarea>
        <br><button type="submit">Tweet</button>
    </form>
</template>

<script>

export default {
    name: 'TweetCreate',
    data() {
        return {
            content: ''
        }
    },
    methods: {
        postTweet() {
            this.$axios.request({
                method: 'POST',
                url: 'https://tweeterest.ml/api/tweets',
                data: {
                    loginToken: this.loginToken(),
                    content: this.content
                }
            })
            .then((response) => {               
                if (response.status === 201) {
                    this.content = '';
                    this.$emit('tweetCreated');
                }
            })
        }
    }
}
</script>

<style lang="scss" scoped>

</style>