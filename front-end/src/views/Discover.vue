<template>
    <div id="discover">
        <h1>Discover</h1>
        <tweet v-for="tweet in tweetsNewestFirst" 
            :key="tweet.tweetId" 
            :tweet="tweet"
            @tweetDeleted="loadTweets"
            @tweetUpdated="loadTweets">
        </tweet>
        <p v-if="!tweets.length">Nothing to show!</p>
    </div>
</template>

<script>
import Tweet from '@/components/Tweet';

export default {
    name: 'Discover',
    components: { 
        Tweet
    },
    data() {
        return {
            limit: 15,
            tweets: []
        }
    },
    computed: {
        tweetsNewestFirst() {
            return this.tweets
            // return this.tweets.slice(0, this.limit).reverse();
        }
    },
    mounted() {
        this.loadTweets();
    },
    methods: {
        loadTweets() {
            this.$axios.request({
                method: 'GET',
                url: 'https://tweeterest.ml/api/tweets',
            })
            .then((response) => {
                if (response.status === 200) {
                    this.tweets = response.data;
                }
            })
        }
    }
}
</script>

<style lang="scss" scoped>

</style>