<template>
    <article>
        <h5>{{ this.comment.username }}</h5>
        <p v-if="editing">
            <textarea v-model="newContent"></textarea>
            <button @click="saveChanges">Save</button>
            <button @click="cancelEdit">Cancel</button>
        </p>
        <p v-else>{{ this.comment.content }}</p>
        <div v-if="owner">
            <button @click="editing=true">Edit</button>
            <button @click="deleteComment">Delete</button>
        </div>
        <tweet-comment-like :commentId="comment.commentId"></tweet-comment-like>
    </article>
</template>

<script>
import TweetCommentLike from './TweetCommentLike'

export default {
    name: 'TweetComment',
    props: [ 'comment' ],
    components: { TweetCommentLike },
    data(){ 
        return {
            editing: false,
            newContent: ''
        }
    },
    computed: {
        owner() {
            return this.comment.userId === this.loggedInUser().userId;
        }
    },
    mounted() {
        this.newContent = this.comment.content;
    },
    methods: {
        cancelEdit() {
            this.newContent = this.comment.content;
            this.editing = false;
        },
        deleteComment() {
            const confirmDelete = confirm('Are you sure you want to delete this comment?');
            if (confirmDelete) {
                this.$axios.request({
                    method: 'DELETE',
                    url: 'https://tweeterest.ml/api/comments',
                    data: {
                        loginToken: this.loginToken(),
                        commentId: this.comment.commentId
                    }
                })
                .then(() => {
                    this.$emit('commentDeleted')
                })
            }
        },
        saveChanges() {
            this.$axios.request({
                method: 'PATCH',
                url: 'https://tweeterest.ml/api/comments',
                data: {
                    loginToken: this.loginToken(),
                    commentId: this.comment.commentId,
                    content: this.newContent
                }
            })
            .then(() => {
                this.editing = false;
                this.$emit('commentUpdated')
            })
        }
    }
}
</script>
