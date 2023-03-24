<template>
    <div class="container">
        <div class="row header">
            <span>题库名:{{data.title}}</span><span>考试截止时间{{data.exam_end_time}}</span>
        </div>
        <div class="row content" v-for="(item, index) in data.subjects_list">
            <div class="col-md-6">
                <span>题目{{index+1}}、{{item.question}}</span>
            </div>
            <div>
                <el-input
                        v-model='item.answer'
                        type="textarea"
                        :rows="2"
                        placeholder="请答题">
                </el-input>
            </div>
        </div>
        <div class="footer">
            <el-button type="primary" size="small" @click="handleCommitPaper">提交考卷</el-button>
            <el-button type="primary" size="small" @click="handleGoBack">返回上一页面</el-button>
        </div>
    </div>
</template>

<script>
    export default {
        name: "ExamView",
        data() {
            return {
                test_bank_id: this.$route.query.test_bank_id,
                data: {},
                student_id: Number(this.$cookies.get('user_id')),
                role_id: this.$cookies.get('role_id'),
                token: this.$cookies.get('token'),
                answer: '',
            }
        },
        methods: {
            handleGoBack() {
                this.$router.go(-1)
            },

            // test() {
            //     console.log(this.data.subjects_list)
            //     this.answer = JSON.stringify(this.data.subjects_list)
            //     console.log(this.answer)
            //     console.log(typeof(this.answer))
            // }

            // 提交考卷
            handleCommitPaper() {
                this.answer = JSON.stringify(this.data.subjects_list)
                // 'http://127.0.0.1:8000/students/student-paper/'
                this.$axios.post(this.$settings.base_url + `students/student-paper/?role_id=${this.role_id}`, {
                    'test_bank': this.test_bank_id,
                    'students': this.student_id,
                    'answer': this.answer,
                }, {headers: {'Authorization': `jwt ${this.token}`}}).then(response => {
                    if (response.data.status == 100) {
                        this.$message({
                            type: 'success',
                            message: '提交成功',
                            duration: 1000,
                            onClose: () => {
                                this.$router.go(-1)
                            }
                        })
                    } else {
                        this.$message('提交失败,你可能是已经提交过一遍了')
                    }
                })
            },

            // 自动提交考卷
            handleAutoCommitPaper() {
                let exam_end_time = this.data.exam_end_time
                let e_time = Date.parse(exam_end_time)  // 得到考试截止时间时间戳
                // console.log(exam_end_time)
                // console.log(e_time)
                let c_time = Date.parse(new Date())  // 得到当前时间的时间戳
                // console.log(c_time)
                let r_time = e_time - c_time - 2000  // 1秒是在后端结束考试时先把试卷提交
                console.log(r_time)
                setTimeout(() => {
                    this.$message({
                        type: 'info',
                        message: '考试时间到,正在提交',
                        duration: 500,
                        onClose: () => {
                            this.handleCommitPaper()
                        }
                    })
                }, r_time)  // 毫秒
                console.log('自动交卷功能激活')
            },

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

            // 要三秒的延迟
            // 触发自动提交试卷功能
            setTimeout(() => {
                this.handleAutoCommitPaper()
            }, 1000)

            let test_bank_id = this.$route.query.test_bank_id
            // 'http://127.0.0.1:8000/students/test-bank/8/'
            this.$axios.get(this.$settings.base_url + `students/test-bank/${test_bank_id}/?role_id=${this.role_id}`, {
                headers: {'Authorization': `jwt ${this.token}`}
            }).then(response => {
                // console.log(response.data)
                this.data = response.data
            }).catch(error => {
                console.log(error)
            })
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