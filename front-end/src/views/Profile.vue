<template>
    <div id="profile">
        <div v-if="user">
            <h1>{{ user.username }}'s Profile</h1>
            <p>{{ user.brithdate }}</p>
            <p>{{ user.email }}</p>
            <p>{{ user.bio }}</p>
            <div v-if="!owner">
                <follow-button :userId="user.userId"></follow-button>
            </div>
            <hr>
            <div v-if="owner">
                <button @click="editing=true">Edit Bio</button>
                <hr>
                <div v-if="editing">
                    <textarea v-model="newContent"></textarea>
                    <button @click="saveChanges">Save</button>
                    <button @click="cancelEdit">Cancel</button>
                    <hr>
                </div>
                <tweet-create @tweetCreated="loadTweets"></tweet-create>
                <hr>
            </div>
            <div v-if="tweets.length">
                <tweet v-for="tweet in tweets" :key="tweet.tweetId" :tweet="tweet"></tweet>
            </div>
            
        </div>
    </div>
</template>

<script>
import FollowButton from '@/components/FollowButton';
import Tweet from '@/components/Tweet';
import TweetCreate from '@/components/TweetCreate';

export default {
    name: 'Profile',
    components: {
        FollowButton,
        Tweet,
        TweetCreate
    },
    data() {
        return {
            editing: false,
            newContent: '',
            user: null,
            tweets: []         
        }
    },
    computed: {
        owner() {
            return this.user.userId === this.loggedInUser().userId
        },
        profileId() {
            return this.$route.params.id || this.$cookies.get('user').userId
        }
    },
    mounted() {
        this.loadUser();
    },
    methods: {
        cancelEdit() {
            this.newContent = this.user.bio
            this.editing = false
        },
        loadTweets() {
            this.$axios.request({
                method: 'GET',
                url: 'https://tweeterest.ml/api/tweets',
                params: {
                    userId: this.profileId
                }
            })
            .then((response) => {
                this.tweets = response.data
            })
        },
        loadUser() {
            this.$axios.request({
                method: 'GET',
                url: 'https://tweeterest.ml/api/users',
                params: {
                    userId: this.profileId
                }
            })
            .then((response) => {
                this.user = response.data[0]
                this.newContent = this.user.bio
                this.loadTweets(this.profileId)
            })
        },
        saveChanges() {
            this.$axios.request({
                method: 'PATCH',
                url: 'https://tweeterest.ml/api/users',
                data: {
                    loginToken: this.loginToken(),
                    bio: this.newContent
                }
            })
            .then(() => {
                this.editing = false;
                this.user.bio = this.newContent;
            })
        }
    }
}
</script>
