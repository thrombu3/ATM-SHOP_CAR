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
            题目{{index+1}}分数：
            <div class="col-md-1">
                <el-input v-model="item.source" @input="numValid(item,item.source)" placeholder="输入数字"></el-input>
            </div>
        </div>
        <div class="row">
            <div class="col-md-1 col-md-offset-5">
                <h2>总分数</h2>
                <el-input v-model=source_total placeholder="自动填充" disabled></el-input>
            </div>
        </div>
        <div class="footer">
            <el-button type="primary" size="small" @click="handleCommit">提交</el-button>
            <el-button type="primary" size="small" @click="handleGoBack">返回上一页面</el-button>
        </div>
    </div>
</template>

<script>
    export default {
        name: "EditPaperView",
        data() {
            return {
                paper_id: this.$route.query.paper_id,
                data: {},
                teacher_id: Number(this.$cookies.get('user_id')),
                role_id: this.$cookies.get('role_id'),
                token: this.$cookies.get('token'),
                answer_list: [],
                source_total: '0',
            }
        },
        methods: {
            numValid(item, source) {
                //只能输入数字
                // console.log(source)
                if (!Number(source)) {
                    item.source = ''
                }
                // 计算总分数
                this.source_total = '0';
                this.answer_list.forEach(subject => {
                    if (subject.source) {
                        this.source_total = Number(this.source_total) + Number(subject.source)
                    }
                })
            },

            handleGoBack() {
                this.$router.go(-1)
            },

            // 提交批阅
            handleCommit() {
                // 'http://127.0.0.1:8000/teachers/teachers-edit-paper/1/?teacher_id=1' put
                this.$axios.put(this.$settings.base_url + `teachers/teachers-edit-paper/${this.paper_id}/?teacher_id=${this.teacher_id}&role_id=${this.role_id}`, {
                    'source': Number(this.source_total),
                    'is_check': true
                }, {
                    headers: {'Authorization': `jwt ${this.token}`}
                }).then(response => {
                    // console.log(response)
                    if (response.data.status == 100) {
                        this.$message({
                            type: 'success',
                            message: '修改成功!',
                            duration: 1000
                        })
                        this.$router.go(-1)
                    } else {
                        this.$message({
                            type: 'error',
                            message: response.data.msg,
                            duration: 1000
                        })
                    }
                }).catch(error => {
                    console.log(error)
                })
            }
        },
        mounted() {
            // 权限校验
            // let role_id = this.$cookies.get('role_id')
            // if (role_id != '1') {
            //     this.$message({
            //     type: 'warning',
            //     duration: 1000,
            //     message: '你不是老师,没有权限'
            // });
            //     this.$router.go(-1)
            // }

            // 'http://127.0.0.1:8000/teachers/teachers-edit-paper/1/?teacher_id=1'  get
            this.$axios.get(this.$settings.base_url + `teachers/teachers-edit-paper/${this.paper_id}/?teacher_id=${this.teacher_id}&role_id=${this.role_id}`, {
                headers: {'Authorization': `jwt ${this.token}`}
            }).then(response => {
                this.data = response.data
                this.answer_list = JSON.parse(response.data.answer)
                // console.log(this.answer_list)
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