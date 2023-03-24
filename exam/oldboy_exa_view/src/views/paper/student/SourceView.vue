<template>
    <div class="container">
        <div class="row header">
            <span>题库名:{{data.test_bank_name}}</span>
            <span>出卷老师:{{data.teachers_name}}</span>
            <span>考卷提交时间{{data.commit_time}}</span>
        </div>
        <div class="row content" v-for="(item, index) in this.answer_list">
            <div class="col-md-7">
                <span>题目{{index+1}}、{{item.question}}</span>
            </div>
            <div class="col-md-7">
                <span>答案:{{item.answer}}</span>
            </div>
        </div>
        <div class="footer">
            <h1>成绩:{{data.source}}</h1>
            <h3>批卷老师:{{data.teachers_name}}</h3>
            <hr>
            <el-button type="primary" size="small" @click="handleGoBack">返回上一页面</el-button>
        </div>
    </div>
</template>

<script>
    export default {
        name: "SourceView",
        data() {
            return {
                paper_id: this.$route.query.paper_id,
                data: {},
                student_id: Number(this.$cookies.get('user_id')),
                role_id: this.$cookies.get('role_id'),
                token: this.$cookies.get('token'),
                answer_list: [],
            }
        },
        mounted() {
            // 权限校验
            // let role_id = this.$cookies.get('role_id')
            // if (role_id != '2') {
            //     this.$message({
            //     type: 'warning',
            //     duration: 1000,
            //     message: '你不是学生,没有权限'
            // });
            //     this.$router.go(-1)
            // }

            // 'http://127.0.0.1:8000/students/student-paper/9/?student_id=1'
            this.$axios.get(this.$settings.base_url + `students/student-paper/${this.paper_id}/?student_id=${this.student_id}&role_id=${this.role_id}`, {
                headers: {'Authorization': `jwt ${this.token}`}
            }).then(response => {
                // console.log(response.data)
                this.data = response.data
                this.answer_list = JSON.parse(response.data.answer)
            }).catch(error => {
                console.log(error)
            })
        },
        methods: {
            handleGoBack() {
                this.$router.go(-1)
            },


        },
    }
</script>

<style scoped>
    .header {
        font-weight: bold;
        font-size: 30px;
    }

    .content {
        font-size: 20px;
        margin-top: 10px;
        font-weight: bold;
    }

    .footer {
        margin-top: 100px;
    }
</style>