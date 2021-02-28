<template>
    <div>
        <hr>
        <tweet-comment v-for="comment in comments" 
            :key="comment.commentId" 
            :comment="comment" 
            @commentDeleted="loadComments"
            @commentUpdated="loadComments">
        </tweet-comment>
        <hr>
        <form @submit.prevent="addComment">
            <textarea v-model="newComment" placeholder="Write a comment..."></textarea>
            <button type="submit">Send</button>
        </form>
    </div>
</template>

<script>
import TweetComment from './TweetComment';

export default {
    name: 'TweetComments',
    props: [ 'tweetId' ],
    components: { TweetComment },
    data() {
        return {
            comments: [],
            newComment: ''
        }
    },
    mounted() {
        this.loadComments()
    },
    methods: {
        addComment() {
            this.$axios.request({
                method: 'POST',
                url: 'https://tweeterest.ml/api/comments',
                data: {
                    loginToken: this.loginToken(),
                    tweetId: this.tweetId,
                    content: this.newComment,
                }
            })
            .then((response) => {
                if (response.status === 200) {
                    // success path
                    this.newComment = ''
                    this.loadComments()
                }
            });
        },
        loadComments() {
            this.$axios.request({
                method: 'GET',
                url: 'https://tweeterest.ml/api/comments',
                params: {
                    tweetId: this.tweetId
                }
            })
            .then((response) => {
                if (response.status === 200) {
                    this.comments = response.data;
                } else {
                    alert('ERROR');
                }
            })
        }
    }
}
</script>

<style lang="scss" scoped>

</style>