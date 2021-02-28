<template>
    <article>
        <strong>
            <router-link :to="'/profile/' + tweet.userId">{{ tweet.username }}</router-link>
        </strong> - <em>{{ tweet.createdAt }}</em>

        <p v-if="editing" >
            <textarea v-model="newContent"></textarea>
            <br><button @click="saveChanges">Save</button>
            <button @click="cancelEdit">Cancel</button>
        </p>
        <p v-else>{{ tweet.content }}</p>
        <div>
            <tweet-like :tweetId="tweet.tweetId"></tweet-like>
            <button @click="toggleComments"> {{ showComments ? 'Hide Comments' : 'Show Comments' }}</button>
        </div>
        <div v-if="owner">
            <button @click="editing=true">Edit</button>
            <button @click="deleteTweet">Delete</button>
        </div>
        
        <tweet-comments v-if="showComments" :tweetId="tweet.tweetId"></tweet-comments>
    </article>
</template>

<script>
import TweetLike from './TweetLike';
import TweetComments from './TweetComments';

export default {
    name: 'Tweet',
    props: [ 'tweet' ],
    components: {
        TweetComments,
        TweetLike
    },
    computed: {
        owner() {
            return this.tweet.userId === this.loggedInUser().userId
        }
    },
    data() {
        return {
            editing: false,
            newContent: '',
            showComments: false
        }
    },
    mounted() {
        this.newContent = this.tweet.content
    },
    methods: {
        cancelEdit() {
            this.newContent = this.tweet.content;
            this.editing = false;
        },
        deleteTweet() {
            const confirmDelete = confirm('Are you sure you want to delete this Tweet?');
            if (confirmDelete) {
                this.$axios.request({
                    method: 'DELETE',
                    url: 'https://tweeterest.ml/api/tweets',
                    data: {
                        loginToken: this.loginToken(),
                        tweetId: this.tweet.tweetId
                    }
                })
                .then((response) => {
                    if (response.status === 204) {
                        // successful path
                        this.$emit('tweetDeleted')
                    }
                })
            }
        },
        saveChanges() {
            this.$axios.request({
                method: 'PATCH',
                url: 'https://tweeterest.ml/api/tweets',
                data: {
                    loginToken: this.loginToken(),
                    tweetId: this.tweet.tweetId,
                    content: this.newContent
                }
            })
            .then((response) => {
                if (response.status === 200) {
                    this.editing = false;
                    this.$emit('tweetUpdated', this.newContent);
                } else {
                    alert('ERROR')
                }
            })
        },
        toggleComments() {
            this.showComments = !this.showComments
        }
    }
}
</script>

<style lang="scss" scoped>

</style>