<template>
    <div class="time">
        <section class="remind">
            <span>当前时间: </span>
            <span>{{ now_date_time }}</span>
            <span>星期{{ now_week_time }}</span>
            <span>{{ now_specific_time }}</span>
        </section>
    </div>
</template>

<script>
    export default {
        name: "nowtime",
        data() {
            return {
                myDate: '',
                now_date_time: '',
                now_specific_time: '',
                now_week_time: '',
            }
        },
        created() {
            setInterval(() => {
                this.myDate = new Date()
                this.now_date_time = this.myDate.toLocaleDateString()
                this.now_specific_time = this.myDate.toLocaleTimeString()
                this.now_week_time = this.myDate.getDay()
            }, 1000);
        },

    }
</script>

<style scoped>
    .remind {
        border-radius: 4px;
        padding: 10px 30px;
        display: flex;
        position: fixed;
        right: 20px;
        bottom: 5%;
        flex-direction: column;
        color: #606266;
        background-color: #E7F6F6;
        border-left: 4px solid #9efcd0;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    }
</style>